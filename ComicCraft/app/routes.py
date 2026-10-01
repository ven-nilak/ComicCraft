from flask import Blueprint, render_template, request, jsonify
import re

try:
    from .services.gemini_flash import generate_comic_story
    from .services.image_gen import generate_panel_image
except ImportError:
    from app.services.gemini_flash import generate_comic_story
    from app.services.image_gen import generate_panel_image

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        if not prompt:
            return jsonify({'story': 'Please enter a prompt da!', 'images': []})
        
        story = generate_comic_story(prompt)
        
        # Panel ah pirikkurom da
        panels = re.split(r'\*\*Panel \d+\*\*', story, flags=re.IGNORECASE)
        panels = [p.strip() for p in panels if p.strip()][:6]

        images = []
        for i, panel_text in enumerate(panels, 1):
            # Visual mattum extract pannurom da - ithu than main fix!
            visual_match = re.search(r'\*\*Visual:\*\*(.*?)\*\*Caption:', panel_text, re.DOTALL | re.IGNORECASE)
            if visual_match:
                desc = visual_match.group(1).strip()
            else:
                # Visual illa na first 2 line eduthukalam
                desc = panel_text[:250]
            
            # Symbols ellam clean pannurom da
            desc = desc.replace('*', '').replace('"', '').strip()
            # Panel ku unique ah comic style add pannurom
            final_prompt = f"{desc}, comic book panel, cartoon style, vibrant colors, detailed"
            
            img_url = generate_panel_image(final_prompt, i)
            images.append(img_url)

        return jsonify({'story': story, 'images': images})
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({'story': f"Error: {str(e)}", 'images': []})
        