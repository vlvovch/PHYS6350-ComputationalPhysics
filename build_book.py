import os
import subprocess
import shutil

def load_env(env_path):
    env = {}
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    env[key.strip()] = value.strip()
    return env

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, '.env.local')
    env = load_env(env_path)

    ga_id = env.get('GOOGLE_ANALYTICS_ID', '')
    umami_url = env.get('UMAMI_SCRIPT_URL', '')
    umami_id = env.get('UMAMI_WEBSITE_ID', '')
    plausible_url = env.get('PLAUSIBLE_SCRIPT_URL', '')
    swetrix_pid = env.get('SWETRIX_PROJECT_ID', '')
    swetrix_api = env.get('SWETRIX_API_URL', '')

    print(f"Injecting credentials: GA_ID={ga_id}, UMAMI_URL={umami_url}, PLAUSIBLE_URL={plausible_url}, SWETRIX_PID={swetrix_pid}")

    # 1. Generate umami.js
    template_path = os.path.join(base_dir, 'book', '_static', 'umami.js.template')
    output_js_path = os.path.join(base_dir, 'book', '_static', 'umami.js')

    with open(template_path, 'r') as f:
        js_content = f.read()
    
    js_content = js_content.replace('__UMAMI_SCRIPT_URL__', umami_url)
    js_content = js_content.replace('__UMAMI_WEBSITE_ID__', umami_id)

    with open(output_js_path, 'w') as f:
        f.write(js_content)
    
    print(f"Generated {output_js_path}")

    # 1b. Generate plausible.js
    template_path_plausible = os.path.join(base_dir, 'book', '_static', 'plausible.js.template')
    output_js_path_plausible = os.path.join(base_dir, 'book', '_static', 'plausible.js')

    if os.path.exists(template_path_plausible):
        with open(template_path_plausible, 'r') as f:
            js_content_plausible = f.read()
        
        js_content_plausible = js_content_plausible.replace('__PLAUSIBLE_SCRIPT_URL__', plausible_url)

        with open(output_js_path_plausible, 'w') as f:
            f.write(js_content_plausible)
        
        print(f"Generated {output_js_path_plausible}")

    # 1c. Generate swetrix html content
    template_path_swetrix = os.path.join(base_dir, 'book', '_static', 'swetrix.html.template')
    swetrix_html = ""
    if os.path.exists(template_path_swetrix):
        with open(template_path_swetrix, 'r') as f:
            swetrix_html = f.read()
        
        swetrix_html = swetrix_html.replace('__SWETRIX_PROJECT_ID__', swetrix_pid)
        swetrix_html = swetrix_html.replace('__SWETRIX_API_URL__', swetrix_api)
        
        # Indent for YAML inclusion (4 spaces as per _config.yml)
        swetrix_html = "\n".join(["    " + line if line.strip() else line for line in swetrix_html.split("\n")])

    # 2. Generate _config_secret.yml
    config_path = os.path.join(base_dir, 'book', '_config.yml')
    secret_config_path = os.path.join(base_dir, 'book', '_config_secret.yml')

    with open(config_path, 'r') as f:
        config_content = f.read()

    # Replace placeholders
    config_content = config_content.replace('google_analytics_id        : ""', f'google_analytics_id        : "{ga_id}"')
    config_content = config_content.replace('__SWETRIX_CONTENT__', swetrix_html)

    with open(secret_config_path, 'w') as f:
        f.write(config_content)
    
    print(f"Generated {secret_config_path}")

    # 3. Run Build
    try:
        cmd = 'jupyter-book build book --config book/_config_secret.yml'
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Build failed!")
        exit(1)
    finally:
        # Cleanup
        if os.path.exists(secret_config_path):
            os.remove(secret_config_path)
            print(f"Removed {secret_config_path}")
        # We might want to keep umami.js or remove it. Keeping it is fine as it is ignored/overwritten.

if __name__ == "__main__":
    main()
