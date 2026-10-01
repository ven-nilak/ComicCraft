import random
import urllib.parse

def generate_panel_image(panel_text, panel_num):
    text = panel_text.lower()
    seed = random.randint(1, 999999) + (panel_num * 100)

    def get_cartoon(prompt):
        # Ella pic um cute toy / cartoon style la varum - 100% safe!
        safe_prompt = f"cute 3d toy style, chibi, kawaii, {prompt}, soft pastel colors, childrens storybook illustration, pixar style"
        encoded = urllib.parse.quote(safe_prompt)
        return f"https://image.pollinations.ai/prompt/{encoded}?width=512&height=512&seed={seed}&nologo=true&model=turbo&safe=true"

    # 1. DOGS
    if any(x in text for x in ["dog", "puppy", "husky", "labrador"]):
        return f"https://placedog.net/512/512?random={seed}"

    # 2. CATS - un favourite!
    elif any(x in text for x in ["cat", "kitten", "meow"]):
        return f"https://cataas.com/cat/cute?width=512&height=512&{seed}"

    # 3. BIRDS
    elif any(x in text for x in ["bird", "parrot", "crow", "sparrow", "peacock", "owl", "pigeon"]):
        return get_cartoon(f"cute little {text[:50]} bird, fluffy feathers")

    # 4. OTHER ANIMALS
    elif any(x in text for x in ["rabbit", "elephant", "lion", "tiger", "bear", "monkey", "cow", "mouse", "fox"]):
        return get_cartoon(f"cute baby {text[:50]} animal")

    # 5. NATURE SCENE
    elif any(x in text for x in ["forest", "mountain", "beach", "river", "nature", "jungle", "garden", "sky", "sunset", "rain"]):
        return get_cartoon(f"beautiful {text[:60]} landscape, magical nature scene")

    # 6. CREATIVE HUMAN BEINGS - TOY MAATHIRI!
    elif any(x in text for x in ["boy", "girl", "man", "woman", "human", "kid", "child", "detective", "king", "queen", "superhero"]):
        return get_cartoon(f"cute chibi toy doll of {text[:60]}, little figure, clay toy style, big head small body")

    # 7. DEFAULT - ethuvume match aagalana cute cartoon
    else:
        return get_cartoon(text[:80])
