import os
import psutil
import subprocess

class ScriptRunner:
    
    def __init__(self, script_name, code, language):
        self.script_name = script_name
        self.code = code
        self.language = language
        self.timeout = 10
        self.temp_dir = '/home/mhm101/LeetCodeApp/LeetCodeHQ/temp'

    def create_file(self):
        temp_file_path = os.path.join(self.temp_dir, f"{self.script_name}.{self.language}")
        with open(temp_file_path, "w") as file:
            file.write(self.code)

    def run_script(self):
        
        if self.language.lower() == 'py':
            command = f"python {os.path.join(self.temp_dir, self.script_name)}.py"
            output_file_path = os.path.join(self.temp_dir, f"{self.script_name}.txt")
            with open(output_file_path, 'w') as f:
                process = subprocess.Popen(command, shell=True, stdout=f, stderr=f)
                try:
                    process.wait(timeout=self.timeout)
                except subprocess.TimeoutExpired:
                    with open(output_file_path, 'w') as f:
                        f.write("\nTime Out ! Script terminated.\n")
                        f.flush()
                    process.kill()
                    
        elif self.language.lower() == 'cpp':
            command_compile = f"g++ {os.path.join(self.temp_dir, self.script_name)}.cpp -o {os.path.join(self.temp_dir, self.script_name)}.exe"
            command_run = f"{os.path.join(self.temp_dir, self.script_name)}.exe"
            try:
                subprocess.check_call(command_compile, shell=True)
                output_file_path = os.path.join(self.temp_dir, f"{self.script_name}.txt")
                with open(output_file_path, 'w') as f:
                    process = subprocess.Popen(command_run, shell=True, stdout=f, stderr=f)
                    try:
                        process.wait(timeout=self.timeout)
                    except subprocess.TimeoutExpired:
                        with open(output_file_path, 'w') as f:
                            f.write("\nTime Out ! Script terminated.\n")
                            f.flush()
                        process.kill()

            except subprocess.CalledProcessError as e:
                output_file_path = os.path.join(self.temp_dir, f"{self.script_name}.txt")
                with open(output_file_path, 'w') as f:
                    f.write(f"Compilation error: {e}\n")
        
        else:
            output_file_path = os.path.join(self.temp_dir, f"{self.script_name}.txt")
            with open(output_file_path, 'w') as f:
                f.write("Unsupported language.\n")

    def clean(self):

        files_to_delete = [
            os.path.join(self.temp_dir, f"{self.script_name}.cpp"),
            os.path.join(self.temp_dir, f"{self.script_name}.exe"),
            os.path.join(self.temp_dir, f"{self.script_name}.py"),
            os.path.join(self.temp_dir, f"{self.script_name}.txt"),
        ]

        for file in files_to_delete:
            if os.path.exists(file):
                pid = None
                for proc in psutil.process_iter(['pid', 'name']):
                    try:
                        for item in proc.open_files():
                            if item.path == file:
                                pid = proc.info['pid']
                                break
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

                if pid is not None:
                    proc = psutil.Process(pid)
                    proc.terminate()
                    print(f"Terminated process {pid} holding file {file} open")

                os.remove(file)
                print(f"Deleted file: {file}")
            else:
                print(f"File not found: {file}")

    def run(self):
        self.create_file()
        self.run_script()