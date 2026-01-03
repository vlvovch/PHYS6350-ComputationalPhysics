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

    print(f"Injecting credentials: GA_ID={ga_id}, UMAMI_URL={umami_url}")

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

    # 2. Generate _config_secret.yml
    config_path = os.path.join(base_dir, 'book', '_config.yml')
    secret_config_path = os.path.join(base_dir, 'book', '_config_secret.yml')

    with open(config_path, 'r') as f:
        config_content = f.read()

    # Replace the empty placeholder or specific key
    # We look for: google_analytics_id        : ""
    config_content = config_content.replace('google_analytics_id        : ""', f'google_analytics_id        : "{ga_id}"')

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
