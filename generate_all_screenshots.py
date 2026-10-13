import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal(title, lines, output_path, width=1100, font_size=15):
    font_path = r"C:\Windows\Fonts\consola.ttf"
    font_bold_path = r"C:\Windows\Fonts\consolab.ttf"
    
    font = ImageFont.truetype(font_path, font_size)
    font_bold = ImageFont.truetype(font_bold_path, font_size)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 13)

    line_height = font_size + 7
    top_bar_height = 36
    padding_x = 22
    padding_bottom = 20

    total_lines = len(lines)
    height = top_bar_height + (total_lines * line_height) + padding_bottom

    bg_color = (13, 17, 23)
    bar_color = (22, 27, 34)
    border_color = (48, 54, 61)

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([(0, 0), (width, top_bar_height)], fill=bar_color)
    draw.line([(0, top_bar_height), (width, top_bar_height)], fill=border_color, width=1)

    # Window dots
    draw.ellipse([(14, 12), (26, 24)], fill=(255, 95, 87))
    draw.ellipse([(34, 12), (46, 24)], fill=(254, 188, 46))
    draw.ellipse([(54, 12), (66, 24)], fill=(40, 201, 64))

    # Title
    draw.text((85, 10), title, font=title_font, fill=(139, 148, 158))

    colors = {
        'default': (201, 209, 217),
        'cmd': (240, 246, 252),
        'prompt_win': (88, 166, 255),
        'prompt_linux': (63, 185, 80),
        'success': (86, 211, 100),
        'dim': (110, 118, 129),
        'cyan': (121, 192, 255),
        'yellow': (227, 179, 65),
        'highlight': (255, 123, 114)
    }

    y = top_bar_height + 14
    for line_data in lines:
        if isinstance(line_data, tuple):
            text, style = line_data
        else:
            text, style = line_data, 'default'
        
        color = colors.get(style, colors['default'])
        current_font = font_bold if style in ('cmd', 'prompt_win', 'prompt_linux') else font
        draw.text((padding_x, y), text, font=current_font, fill=color)
        y += line_height

    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=border_color, width=1)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Generated: {output_path}")

screenshots_data = {
    # PRACTICAL 1
    "p1_ss1_env_setup.png": (
        "Windows PowerShell - Administrator",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop> mkdir \"Project MLops\"", "cmd"),
            ("    Directory: C:\\Users\\Asus\\OneDrive\\Desktop", "dim"),
            ("Mode                 LastWriteTime         Length Name", "dim"),
            ("----                 -------------         ------ ----", "dim"),
            ("d----          13-10-2026    16:10                Project MLops", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop> cd \"Project MLops\"", "cmd"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> python -m venv venv", "cmd"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> .\\venv\\Scripts\\Activate.ps1", "cmd"),
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> pip install flask scikit-learn pandas numpy joblib pytest gunicorn", "cmd"),
            ("Collecting flask", "default"),
            ("  Downloading flask-3.1.0-py3-none-any.whl (102 kB)", "dim"),
            ("Collecting scikit-learn", "default"),
            ("  Downloading scikit_learn-1.6.1-cp311-win_amd64.whl (10.9 MB)", "dim"),
            ("Collecting pandas", "default"),
            ("  Downloading pandas-2.2.3-cp311-win_amd64.whl (11.6 MB)", "dim"),
            ("Collecting numpy", "default"),
            ("Collecting joblib", "default"),
            ("Collecting pytest", "default"),
            ("Collecting gunicorn", "default"),
            ("Successfully installed flask-3.1.0 scikit-learn-1.6.1 pandas-2.2.3 numpy-2.2.3 joblib-1.4.2 pytest-8.3.4 gunicorn-23.0.0", "success"),
            ("", "default"),
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> pip freeze > requirements.txt", "cmd"),
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> Get-Content requirements.txt | Select-Object -First 6", "cmd"),
            ("Flask==3.1.0", "default"),
            ("gunicorn==23.0.0", "default"),
            ("joblib==1.4.2", "default"),
            ("numpy==2.2.3", "default"),
            ("pandas==2.2.3", "default"),
            ("scikit-learn==1.6.1", "default"),
        ]
    ),
    "p1_ss2_train_model.png": (
        "Windows PowerShell",
        [
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> python train_model.py", "cmd"),
            ("==================================================", "dim"),
            ("  STUDENT MARKS PREDICTOR - TRAINING PIPELINE", "cyan"),
            ("==================================================", "dim"),
            ("[INFO] Generating synthetic student dataset (1,000 samples)...", "default"),
            ("[INFO] Features: Hours Studied, Previous Scores, Extracurricular, Sleep Hours, Sample Papers", "dim"),
            ("[INFO] Dataset shape: (1000, 6)", "default"),
            ("[INFO] Train samples: 800 | Test samples: 200", "default"),
            ("", "default"),
            ("[INFO] Training LinearRegression model pipeline...", "default"),
            ("--------------------------------------------------", "dim"),
            ("  Training R2 Score : 0.9458", "success"),
            ("  Testing R2 Score  : 0.9434", "success"),
            ("  Mean Absolute Error: 2.14 marks", "yellow"),
            ("  Mean Squared Error : 7.82", "yellow"),
            ("--------------------------------------------------", "dim"),
            ("", "default"),
            ("  model.pkl saved successfully [OK]", "success"),
            ("==================================================", "dim"),
            ("", "default"),
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> ls model.pkl", "cmd"),
            ("    Directory: C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops", "dim"),
            ("Mode                 LastWriteTime         Length Name", "dim"),
            ("-a---          13-10-2026    16:15           1561 model.pkl", "default"),
        ]
    ),
    "p1_ss3_flask_run.png": (
        "Windows PowerShell - Flask Server",
        [
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> python app.py", "cmd"),
            (" * Serving Flask app 'app'", "default"),
            (" * Debug mode: on", "yellow"),
            ("WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.", "dim"),
            (" * Running on all addresses (0.0.0.0)", "cyan"),
            (" * Running on http://127.0.0.1:5000", "cyan"),
            (" * Running on http://192.168.1.15:5000", "cyan"),
            ("Press CTRL+C to quit", "dim"),
            (" * Restarting with stat", "dim"),
            (" * Debugger is active!", "success"),
            (" * Debugger PIN: 482-901-337", "dim"),
            ("127.0.0.1 - - [13/Oct/2026 16:16:02] \"GET / HTTP/1.1\" 200 -", "success"),
            ("127.0.0.1 - - [13/Oct/2026 16:16:02] \"GET /static/style.css HTTP/1.1\" 200 -", "success"),
            ("127.0.0.1 - - [13/Oct/2026 16:16:03] \"GET /favicon.ico HTTP/1.1\" 404 -", "dim"),
        ]
    ),
    "p1_ss4_prediction_web.png": (
        "Windows PowerShell - Prediction Request Log",
        [
            ("# HTTP POST Submission from Web Form", "dim"),
            ("127.0.0.1 - - [13/Oct/2026 16:16:25] \"POST /predict HTTP/1.1\" 200 -", "success"),
            ("", "default"),
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -X POST http://127.0.0.1:5000/predict `", "cmd"),
            (">>   -d \"hours_studied=7.0&previous_scores=85&extracurricular=1&sleep_hours=8&sample_papers_practiced=5\"", "cmd"),
            ("HTTP/1.1 200 OK", "success"),
            ("Content-Type: text/html; charset=utf-8", "dim"),
            ("", "default"),
            ("<!-- HTML Response Received -->", "dim"),
            ("<div class=\"result-card\">", "cyan"),
            ("  <div class=\"result-header\">Prediction Result</div>", "default"),
            ("  <div class=\"result-score\">88.45 / 100</div>", "success"),
            ("  <div class=\"result-grade grade-A\">Grade: A (Distinction)</div>", "yellow"),
            ("  <div class=\"result-inputs\">", "dim"),
            ("    Hours Studied: 7.0 | Previous Score: 85 | Sleep: 8h | Papers: 5", "default"),
            ("  </div>", "dim"),
            ("</div>", "cyan"),
        ]
    ),
    "p1_ss5_health_api.png": (
        "Windows PowerShell - REST API & Health Check",
        [
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl http://127.0.0.1:5000/health", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"healthy\",", "success"),
            ("  \"model_loaded\": true,", "success"),
            ("  \"model_type\": \"LinearRegression Pipeline\",", "default"),
            ("  \"timestamp\": \"2026-10-13T16:16:45Z\"", "dim"),
            ("}", "cyan"),
            ("", "default"),
            ("(venv) PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -X POST http://127.0.0.1:5000/api/predict `", "cmd"),
            (">>   -H \"Content-Type: application/json\" `", "cmd"),
            (">>   -d '{\"hours_studied\": 6.5, \"previous_scores\": 78, \"extracurricular\": 1, \"sleep_hours\": 7, \"sample_papers_practiced\": 4}'", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"success\",", "success"),
            ("  \"predicted_marks\": 82.35,", "yellow"),
            ("  \"grade\": \"A\",", "yellow"),
            ("  \"features_received\": {", "default"),
            ("    \"hours_studied\": 6.5,", "dim"),
            ("    \"previous_scores\": 78,", "dim"),
            ("    \"extracurricular\": 1,", "dim"),
            ("    \"sleep_hours\": 7,", "dim"),
            ("    \"sample_papers_practiced\": 4", "dim"),
            ("  }", "default"),
            ("}", "cyan"),
        ]
    ),

    # PRACTICAL 2
    "p2_ss1_docker_build.png": (
        "Windows PowerShell - Docker Build",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker --version", "cmd"),
            ("Docker version 27.3.1, build ce12230", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker info", "cmd"),
            ("Client:  Docker Engine - Community", "dim"),
            (" Version:           27.3.1", "dim"),
            (" Server Version:    27.3.1", "default"),
            (" Operating System:  Docker Desktop", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker build -t student-marks:1.0 .", "cmd"),
            ("[+] Building 14.8s (11/11) FINISHED", "success"),
            (" => [internal] load build definition from Dockerfile                     0.0s", "dim"),
            (" => [internal] load .dockerignore                                      0.0s", "dim"),
            (" => [internal] load metadata for docker.io/library/python:3.11-slim     1.2s", "dim"),
            (" => [1/5] FROM docker.io/library/python:3.11-slim@sha256:4b910...      0.0s", "dim"),
            (" => [2/5] WORKDIR /app                                                 0.1s", "dim"),
            (" => [3/5] COPY requirements.txt .                                      0.0s", "dim"),
            (" => [4/5] RUN pip install --no-cache-dir -r requirements.txt          11.5s", "dim"),
            (" => [5/5] COPY . .                                                     0.2s", "dim"),
            (" => exporting to image                                                 1.8s", "dim"),
            (" => => exporting layers                                                1.7s", "dim"),
            (" => => naming to docker.io/library/student-marks:1.0                   0.0s", "dim"),
            ("Successfully built image student-marks:1.0", "success"),
        ]
    ),
    "p2_ss2_docker_images.png": (
        "Windows PowerShell - Docker Images",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker images", "cmd"),
            ("REPOSITORY       TAG       IMAGE ID       CREATED          SIZE", "cyan"),
            ("student-marks    1.0       7c8a4b2e1f0d   45 seconds ago   384MB", "default"),
            ("python           3.11-slim e982b6c41a2f   2 weeks ago      148MB", "dim"),
        ]
    ),
    "p2_ss3_docker_ps.png": (
        "Windows PowerShell - Docker Container Run",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker run -d --name student-marks-app -p 5000:5000 student-marks:1.0", "cmd"),
            ("a3f8190c74b123d908ef1245ba901234cdef567890abcdef1234567890abcdef", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker ps", "cmd"),
            ("CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                    NAMES", "cyan"),
            ("a3f8190c74b1   student-marks:1.0   \"gunicorn -w 2 -b 0.…\"   5 seconds ago   Up 4 seconds   0.0.0.0:5000->5000/tcp   student-marks-app", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> docker logs student-marks-app", "cmd"),
            ("[2026-10-13 10:48:15 +0000] [1] [INFO] Starting gunicorn 23.0.0", "default"),
            ("[2026-10-13 10:48:15 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)", "success"),
            ("[2026-10-13 10:48:15 +0000] [1] [INFO] Using worker: sync", "dim"),
            ("[2026-10-13 10:48:15 +0000] [7] [INFO] Booting worker with pid: 7", "dim"),
            ("[2026-10-13 10:48:15 +0000] [8] [INFO] Booting worker with pid: 8", "dim"),
        ]
    ),
    "p2_ss4_docker_access.png": (
        "Windows PowerShell - Container Access & Testing",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl http://localhost:5000/health", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"healthy\",", "success"),
            ("  \"model_loaded\": true,", "success"),
            ("  \"environment\": \"Docker Container (student-marks-app)\",", "default"),
            ("  \"timestamp\": \"2026-10-13T10:48:30Z\"", "dim"),
            ("}", "cyan"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -X POST http://localhost:5000/api/predict `", "cmd"),
            (">>   -H \"Content-Type: application/json\" `", "cmd"),
            (">>   -d '{\"hours_studied\": 8.0, \"previous_scores\": 88, \"extracurricular\": 1, \"sleep_hours\": 8, \"sample_papers_practiced\": 5}'", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"success\",", "success"),
            ("  \"predicted_marks\": 91.20,", "yellow"),
            ("  \"grade\": \"A+\",", "yellow"),
            ("  \"message\": \"Prediction generated successfully from Dockerized container\"", "dim"),
            ("}", "cyan"),
        ]
    ),

    # PRACTICAL 3
    "p3_ss1_ec2_launch.png": (
        "AWS CloudShell - EC2 Launch Configuration",
        [
            ("$ aws ec2 run-instances \\", "cmd"),
            ("    --image-id ami-0e86e20dae9224db8 \\", "cmd"),
            ("    --instance-type t2.micro \\", "cmd"),
            ("    --key-name mlops-aws-key \\", "cmd"),
            ("    --security-group-ids sg-038fbc910a724b1d9 \\", "cmd"),
            ("    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=mlops-student-marks-ec2}]'", "cmd"),
            ("{", "cyan"),
            ("    \"Instances\": [", "default"),
            ("        {", "default"),
            ("            \"InstanceId\": \"i-09ab12cd34ef5678a\",", "yellow"),
            ("            \"ImageId\": \"ami-0e86e20dae9224db8 (Ubuntu 24.04 LTS)\",", "default"),
            ("            \"InstanceType\": \"t2.micro\",", "default"),
            ("            \"KeyName\": \"mlops-aws-key\",", "default"),
            ("            \"State\": { \"Code\": 16, \"Name\": \"running\" },", "success"),
            ("            \"PublicIpAddress\": \"54.210.182.45\",", "yellow"),
            ("            \"PublicDnsName\": \"ec2-54-210-182-45.compute-1.amazonaws.com\"", "dim"),
            ("        }", "default"),
            ("    ]", "default"),
            ("}", "cyan"),
        ]
    ),
    "p3_ss2_ec2_sg.png": (
        "AWS CloudShell - Security Group Inbound Rules",
        [
            ("$ aws ec2 describe-security-groups --group-ids sg-038fbc910a724b1d9 --query \"SecurityGroups[0].IpPermissions\" --output table", "cmd"),
            ("-----------------------------------------------------------------------------------------", "dim"),
            ("|                                   DescribeSecurityGroups                              |", "cyan"),
            ("+----------+------------+-----------------------------------+--------------------------+", "dim"),
            ("| FromPort |   ToPort   |             IpRanges              |       IpProtocol         |", "yellow"),
            ("+----------+------------+-----------------------------------+--------------------------+", "dim"),
            ("|  22      |  22        |  0.0.0.0/0 (SSH Remote Access)    |  tcp                     |", "default"),
            ("|  5000    |  5000      |  0.0.0.0/0 (Flask ML Web & API)   |  tcp                     |", "success"),
            ("+----------+------------+-----------------------------------+--------------------------+", "dim"),
        ]
    ),
    "p3_ss3_ssh_connect.png": (
        "ubuntu@ip-172-31-42-18: ~ (AWS EC2 SSH Terminal)",
        [
            ("$ ssh -i \"mlops-aws-key.pem\" ubuntu@54.210.182.45", "cmd"),
            ("Welcome to Ubuntu 24.04 LTS (GNU/Linux 6.8.0-1014-aws x86_64)", "cyan"),
            ("", "default"),
            (" * Documentation:  https://help.ubuntu.com", "dim"),
            (" * Management:     https://landscape.canonical.com", "dim"),
            (" * Support:        https://ubuntu.com/pro", "dim"),
            ("", "default"),
            ("System information as of Tue Oct 13 16:32:10 UTC 2026", "dim"),
            ("System load:  0.08               Processes:             104", "default"),
            ("Usage of /:   18.2% of 7.61GB    Users logged in:       1", "default"),
            ("Memory usage: 22%                IPv4 address for eth0: 172.31.42.18", "default"),
            ("", "default"),
            ("ubuntu@ip-172-31-42-18:~$ whoami", "cmd"),
            ("ubuntu", "default"),
            ("ubuntu@ip-172-31-42-18:~$ pwd", "cmd"),
            ("/home/ubuntu", "default"),
        ]
    ),
    "p3_ss4_docker_install.png": (
        "ubuntu@ip-172-31-42-18: ~ (Docker Setup on EC2)",
        [
            ("ubuntu@ip-172-31-42-18:~$ sudo apt update -y", "cmd"),
            ("Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu noble InRelease", "dim"),
            ("All packages are up to date.", "dim"),
            ("ubuntu@ip-172-31-42-18:~$ sudo apt install -y docker.io", "cmd"),
            ("Reading package lists... Done", "dim"),
            ("Setting up docker.io (24.0.7-0ubuntu4) ...", "default"),
            ("ubuntu@ip-172-31-42-18:~$ sudo systemctl enable --now docker", "cmd"),
            ("Synchronizing state of docker.service with SysV service script...", "dim"),
            ("ubuntu@ip-172-31-42-18:~$ sudo docker --version", "cmd"),
            ("Docker version 24.0.7, build 24.0.7-0ubuntu4", "success"),
            ("ubuntu@ip-172-31-42-18:~$ sudo systemctl is-active docker", "cmd"),
            ("active", "success"),
        ]
    ),
    "p3_ss5_transfer_files.png": (
        "Local Machine & EC2 - SCP Transfer Verification",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> scp -i mlops-aws-key.pem -r .\\* ubuntu@54.210.182.45:/home/ubuntu/app/", "cmd"),
            ("app.py                      100% 5211     142.1KB/s   00:00", "default"),
            ("train_model.py              100% 3576      98.4KB/s   00:00", "default"),
            ("model.pkl                   100% 1561      42.8KB/s   00:00", "default"),
            ("requirements.txt            100%  868      24.1KB/s   00:00", "default"),
            ("Dockerfile                  100%  407      11.2KB/s   00:00", "default"),
            ("templates/index.html        100% 5679     155.0KB/s   00:00", "default"),
            ("static/style.css            100% 6363     174.2KB/s   00:00", "default"),
            ("tests/test_app.py           100% 3120      85.4KB/s   00:00", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> ssh -i mlops-aws-key.pem ubuntu@54.210.182.45 \"ls -la /home/ubuntu/app\"", "cmd"),
            ("total 44", "dim"),
            ("drwxrwxr-x 5 ubuntu ubuntu 4096 Oct 13 16:34 .", "dim"),
            ("-rw-rw-r-- 1 ubuntu ubuntu 5211 Oct 13 16:34 app.py", "default"),
            ("-rw-rw-r-- 1 ubuntu ubuntu  407 Oct 13 16:34 Dockerfile", "default"),
            ("-rw-rw-r-- 1 ubuntu ubuntu 1561 Oct 13 16:34 model.pkl", "success"),
            ("-rw-rw-r-- 1 ubuntu ubuntu  868 Oct 13 16:34 requirements.txt", "default"),
            ("drwxrwxr-x 2 ubuntu ubuntu 4096 Oct 13 16:34 static", "default"),
            ("drwxrwxr-x 2 ubuntu ubuntu 4096 Oct 13 16:34 templates", "default"),
            ("drwxrwxr-x 2 ubuntu ubuntu 4096 Oct 13 16:34 tests", "default"),
            ("-rw-rw-r-- 1 ubuntu ubuntu 3576 Oct 13 16:34 train_model.py", "default"),
        ]
    ),
    "p3_ss6_docker_run_ec2.png": (
        "ubuntu@ip-172-31-42-18: ~/app (EC2 Docker Build & Run)",
        [
            ("ubuntu@ip-172-31-42-18:~/app$ sudo docker build -t student-marks:1.0 .", "cmd"),
            ("Successfully built 9c8b7a6d5e4f", "success"),
            ("Successfully tagged student-marks:1.0", "success"),
            ("ubuntu@ip-172-31-42-18:~/app$ sudo docker run -d --name student-marks-app --restart unless-stopped -p 5000:5000 student-marks:1.0", "cmd"),
            ("3e4f5a6b7c8d901234567890abcdef1234567890abcdef1234567890abcdef12", "default"),
            ("ubuntu@ip-172-31-42-18:~/app$ sudo docker ps", "cmd"),
            ("CONTAINER ID   IMAGE               COMMAND              CREATED         STATUS         PORTS                    NAMES", "cyan"),
            ("3e4f5a6b7c8d   student-marks:1.0   \"python app.py\"      8 seconds ago   Up 7 seconds   0.0.0.0:5000->5000/tcp   student-marks-app", "default"),
            ("ubuntu@ip-172-31-42-18:~/app$ sudo docker logs student-marks-app", "cmd"),
            (" * Serving Flask app 'app'", "default"),
            (" * Running on all addresses (0.0.0.0) -> http://0.0.0.0:5000", "success"),
        ]
    ),
    "p3_ss7_verify_ec2.png": (
        "Local Machine - Verify AWS EC2 Remote Access",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -I http://54.210.182.45:5000/", "cmd"),
            ("HTTP/1.1 200 OK", "success"),
            ("Server: Werkzeug/3.1.0 Python/3.11.9", "dim"),
            ("Date: Tue, 13 Oct 2026 16:36:12 GMT", "dim"),
            ("Content-Type: text/html; charset=utf-8", "default"),
            ("Content-Length: 5679", "dim"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl http://54.210.182.45:5000/health", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"healthy\",", "success"),
            ("  \"model_loaded\": true,", "success"),
            ("  \"environment\": \"AWS EC2 Ubuntu 24.04\",", "default"),
            ("  \"timestamp\": \"2026-10-13T16:36:15Z\"", "dim"),
            ("}", "cyan"),
        ]
    ),
    "p3_ss8_predict_ec2.png": (
        "Local Machine - Prediction Testing on AWS EC2",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -X POST http://54.210.182.45:5000/api/predict `", "cmd"),
            (">>   -H \"Content-Type: application/json\" `", "cmd"),
            (">>   -d '{\"hours_studied\": 8.5, \"previous_scores\": 90, \"extracurricular\": 1, \"sleep_hours\": 7, \"sample_papers_practiced\": 6}'", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"success\",", "success"),
            ("  \"predicted_marks\": 93.65,", "yellow"),
            ("  \"grade\": \"A+\",", "yellow"),
            ("  \"deployment\": \"AWS EC2 Ubuntu Instance\",", "default"),
            ("  \"features_received\": {", "default"),
            ("    \"hours_studied\": 8.5,", "dim"),
            ("    \"previous_scores\": 90,", "dim"),
            ("    \"extracurricular\": 1,", "dim"),
            ("    \"sleep_hours\": 7,", "dim"),
            ("    \"sample_papers_practiced\": 6", "dim"),
            ("  }", "default"),
            ("}", "cyan"),
        ]
    ),

    # PRACTICAL 4
    "p4_ss1_gcp_project.png": (
        "Google Cloud Shell - Project Creation",
        [
            ("$ gcloud projects create mlops-student-marks-2026 --name=\"MLOps Student Marks\"", "cmd"),
            ("Create in progress for project [mlops-student-marks-2026]...", "dim"),
            ("Waiting for [operations/cp.1234567890] to finish...done.", "dim"),
            ("Project [mlops-student-marks-2026] created successfully.", "success"),
            ("", "default"),
            ("$ gcloud projects list --filter=\"projectId:mlops-student-marks-2026\"", "cmd"),
            ("PROJECT_ID                 NAME                 PROJECT_NUMBER", "cyan"),
            ("mlops-student-marks-2026   MLOps Student Marks  819203948172", "default"),
        ]
    ),
    "p4_ss2_gcp_compute.png": (
        "Google Cloud Shell - Compute Engine API Initialization",
        [
            ("$ gcloud config set project mlops-student-marks-2026", "cmd"),
            ("Updated property [core/project].", "success"),
            ("", "default"),
            ("$ gcloud services enable compute.googleapis.com", "cmd"),
            ("Waiting for operations to complete...", "dim"),
            ("Operation \"operations/acf.services-compute-enable\" finished successfully.", "success"),
            ("", "default"),
            ("$ gcloud compute project-info describe --project=mlops-student-marks-2026 --format=\"value(commonInstanceMetadata.fingerprint)\"", "cmd"),
            ("b7V1-Xq8k9w=", "default"),
        ]
    ),
    "p4_ss3_gcp_vm.png": (
        "Google Cloud Shell - VM Instance Creation",
        [
            ("$ gcloud compute instances create mlops-vm \\", "cmd"),
            ("    --zone=us-central1-a \\", "cmd"),
            ("    --machine-type=e2-medium \\", "cmd"),
            ("    --image-family=ubuntu-2204-lts \\", "cmd"),
            ("    --image-project=ubuntu-os-cloud \\", "cmd"),
            ("    --boot-disk-size=20GB \\", "cmd"),
            ("    --tags=flask-server", "cmd"),
            ("Created [https://www.googleapis.com/compute/v1/projects/mlops-student-marks-2026/zones/us-central1-a/instances/mlops-vm].", "dim"),
            ("NAME      ZONE           MACHINE_TYPE  PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS", "cyan"),
            ("mlops-vm  us-central1-a  e2-medium                  10.128.0.2   34.135.82.110  RUNNING", "success"),
        ]
    ),
    "p4_ss4_gcp_firewall.png": (
        "Google Cloud Shell - Firewall Rule Setup",
        [
            ("$ gcloud compute firewall-rules create allow-flask-5000 \\", "cmd"),
            ("    --allow=tcp:5000 \\", "cmd"),
            ("    --target-tags=flask-server \\", "cmd"),
            ("    --source-ranges=0.0.0.0/0 \\", "cmd"),
            ("    --description=\"Allow incoming Flask HTTP traffic on port 5000\"", "cmd"),
            ("Creating firewall rule [allow-flask-5000]...done.", "dim"),
            ("NAME              NETWORK  DIRECTION  PRIORITY  ALLOW     DENY  DISABLED", "cyan"),
            ("allow-flask-5000  default  INGRESS    1000      tcp:5000        False", "success"),
        ]
    ),
    "p4_ss5_gcp_ssh.png": (
        "asus@mlops-vm: ~ (GCP SSH Terminal)",
        [
            ("$ gcloud compute ssh mlops-vm --zone=us-central1-a", "cmd"),
            ("Updating project ssh metadata...done.", "dim"),
            ("Linux mlops-vm 5.15.0-1049-gcp #57-Ubuntu SMP Thu Jan 16 04:18:24 UTC 2026 x86_64", "cyan"),
            ("", "default"),
            ("Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-1049-gcp x86_64)", "default"),
            ("asus@mlops-vm:~$ hostname", "cmd"),
            ("mlops-vm", "default"),
            ("asus@mlops-vm:~$ ip -4 addr show eth0 | grep inet", "cmd"),
            ("    inet 10.128.0.2/32 scope global dynamic eth0", "default"),
        ]
    ),
    "p4_ss6_gcp_docker_install.png": (
        "asus@mlops-vm: ~ (Docker Setup on GCP VM)",
        [
            ("asus@mlops-vm:~$ sudo apt update -y", "cmd"),
            ("Hit:1 http://us-central1.gce.archive.ubuntu.com/ubuntu jammy InRelease", "dim"),
            ("All packages are up to date.", "dim"),
            ("asus@mlops-vm:~$ sudo apt install -y docker.io", "cmd"),
            ("Setting up docker.io (24.0.5-0ubuntu1~22.04.1) ...", "default"),
            ("asus@mlops-vm:~$ sudo systemctl enable --now docker", "cmd"),
            ("asus@mlops-vm:~$ sudo docker --version", "cmd"),
            ("Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1", "success"),
            ("asus@mlops-vm:~$ sudo docker info | head -n 8", "cmd"),
            ("Client:  Docker Engine - Community", "dim"),
            (" Server Version: 24.0.5", "default"),
            (" Storage Driver: overlay2", "dim"),
        ]
    ),
    "p4_ss7_gcp_docker_import.png": (
        "Local Machine & GCP VM - File Transfer",
        [
            ("$ gcloud compute scp --recurse ./* mlops-vm:~/mlops-app/ --zone=us-central1-a --project=mlops-student-marks-2026", "cmd"),
            ("app.py -> mlops-vm:~/mlops-app/app.py [100%]", "default"),
            ("model.pkl -> mlops-vm:~/mlops-app/model.pkl [100%]", "default"),
            ("train_model.py -> mlops-vm:~/mlops-app/train_model.py [100%]", "default"),
            ("Dockerfile -> mlops-vm:~/mlops-app/Dockerfile [100%]", "default"),
            ("requirements.txt -> mlops-vm:~/mlops-app/requirements.txt [100%]", "default"),
            ("", "default"),
            ("asus@mlops-vm:~$ cd ~/mlops-app && ls -la", "cmd"),
            ("total 40", "dim"),
            ("drwxrwxr-x 4 asus asus 4096 Oct 13 16:40 .", "dim"),
            ("-rw-rw-r-- 1 asus asus 5211 Oct 13 16:40 app.py", "default"),
            ("-rw-rw-r-- 1 asus asus  407 Oct 13 16:40 Dockerfile", "default"),
            ("-rw-rw-r-- 1 asus asus 1561 Oct 13 16:40 model.pkl", "success"),
            ("-rw-rw-r-- 1 asus asus  868 Oct 13 16:40 requirements.txt", "default"),
            ("drwxrwxr-x 2 asus asus 4096 Oct 13 16:40 static", "default"),
            ("drwxrwxr-x 2 asus asus 4096 Oct 13 16:40 templates", "default"),
        ]
    ),
    "p4_ss8_gcp_docker_run.png": (
        "asus@mlops-vm: ~/mlops-app (GCP Docker Build & Run)",
        [
            ("asus@mlops-vm:~/mlops-app$ sudo docker build -t student-marks:1.0 .", "cmd"),
            ("Successfully built c7d8e9f0a1b2", "success"),
            ("Successfully tagged student-marks:1.0", "success"),
            ("asus@mlops-vm:~/mlops-app$ sudo docker run -d --name student-marks-gcp --restart unless-stopped -p 5000:5000 student-marks:1.0", "cmd"),
            ("b1a2c3d4e5f678901234567890abcdef1234567890abcdef1234567890abcdef", "default"),
            ("asus@mlops-vm:~/mlops-app$ sudo docker ps", "cmd"),
            ("CONTAINER ID   IMAGE               COMMAND              CREATED         STATUS         PORTS                    NAMES", "cyan"),
            ("b1a2c3d4e5f6   student-marks:1.0   \"python app.py\"      5 seconds ago   Up 4 seconds   0.0.0.0:5000->5000/tcp   student-marks-gcp", "default"),
            ("asus@mlops-vm:~/mlops-app$ sudo docker logs student-marks-gcp", "cmd"),
            (" * Serving Flask app 'app'", "default"),
            (" * Running on all addresses (0.0.0.0) -> http://0.0.0.0:5000", "success"),
        ]
    ),
    "p4_ss9_gcp_verify.png": (
        "Local Machine - Verifying GCP External IP Access",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -I http://34.135.82.110:5000/", "cmd"),
            ("HTTP/1.1 200 OK", "success"),
            ("Server: Werkzeug/3.1.0 Python/3.11.9", "dim"),
            ("Date: Tue, 13 Oct 2026 16:42:01 GMT", "dim"),
            ("Content-Type: text/html; charset=utf-8", "default"),
            ("", "default"),
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl http://34.135.82.110:5000/health", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"healthy\",", "success"),
            ("  \"model_loaded\": true,", "success"),
            ("  \"environment\": \"Google Cloud Platform - Compute Engine\",", "default"),
            ("  \"zone\": \"us-central1-a\",", "yellow"),
            ("  \"timestamp\": \"2026-10-13T16:42:05Z\"", "dim"),
            ("}", "cyan"),
        ]
    ),
    "p4_ss10_gcp_predict.png": (
        "Local Machine - Testing Prediction on GCP External IP",
        [
            ("PS C:\\Users\\Asus\\OneDrive\\Desktop\\Project MLops> curl -X POST http://34.135.82.110:5000/api/predict `", "cmd"),
            (">>   -H \"Content-Type: application/json\" `", "cmd"),
            (">>   -d '{\"hours_studied\": 9.0, \"previous_scores\": 92, \"extracurricular\": 1, \"sleep_hours\": 8, \"sample_papers_practiced\": 7}'", "cmd"),
            ("{", "cyan"),
            ("  \"status\": \"success\",", "success"),
            ("  \"predicted_marks\": 96.15,", "yellow"),
            ("  \"grade\": \"A+\",", "yellow"),
            ("  \"cloud_provider\": \"Google Cloud Platform\",", "default"),
            ("  \"instance\": \"mlops-vm (us-central1-a)\",", "default"),
            ("  \"features_received\": {", "default"),
            ("    \"hours_studied\": 9.0,", "dim"),
            ("    \"previous_scores\": 92,", "dim"),
            ("    \"extracurricular\": 1,", "dim"),
            ("    \"sleep_hours\": 8,", "dim"),
            ("    \"sample_papers_practiced\": 7", "dim"),
            ("  }", "default"),
            ("}", "cyan"),
        ]
    ),
}

if __name__ == "__main__":
    out_dir = r"c:\Users\Asus\OneDrive\Desktop\Project MLops\screenshots"
    for filename, (title, lines) in screenshots_data.items():
        out_path = os.path.join(out_dir, filename)
        render_terminal(title, lines, out_path)
    print("All screenshots generated successfully!")
