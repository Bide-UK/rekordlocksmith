import subprocess
import tempfile
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def terminate_rekordbox():
    """
    Terminates any running instances of Rekordbox.
    """
    try:
        # Attempt to kill all Rekordbox processes, suppressing both stdout and stderr.
        subprocess.run(['killall', 'rekordbox'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logging.info("Successfully terminated Rekordbox.")
    except subprocess.CalledProcessError:
        # Ignore the error which occurs if no Rekordbox processes are running.
        pass

def main_operation(target):
    """
    Drives the main operation of the script, with Rekordbox termination before and after the operation.
    """
    logging.warning("\n\nWARNING: All running instances of Rekordbox will be terminated.")
    terminate_rekordbox()  # Terminate Rekordbox before running the operation
    action_sequence = get_action_sequence()
    initiator(action_sequence, target)
    terminate_rekordbox()  # Terminate Rekordbox after running the operation

def get_action_sequence():
    key_phrase_parts = [chr(i) for i in (115, 113, 108, 105, 116, 101, 51, 95, 107, 101, 121)]
    commands = [
        ' '.join(['breakpoint', 'set', '--name', ''.join(key_phrase_parts)]),
        'run',
        'register read rsi',
        'memory read --format s  $rsi',
        'quit'
    ]
    return "\n".join(commands)

def initiator(lldb_actions, app_path):
    try:
        with document(lldb_actions) as instruction_sheet:
            execution_command = formulate_command(app_path, instruction_sheet)
            stdout = conduct_execution(execution_command)
            extracted_information = analyze_output(stdout)
            if extracted_information:
                document_key(extracted_information)
                print(extracted_information)
    except subprocess.CalledProcessError as e:
        logging.error(f"A subprocess error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def document(commands):
    work_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    work_file.write(commands)
    work_file.flush()
    return work_file

def formulate_command(app, instruction_path):
    return ['lldb', app, '-s', instruction_path.name]

def conduct_execution(formation):

    try:
        process = subprocess.Popen(formation, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, formation, output=stdout, stderr=stderr)
        return stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"A subprocess error occurred: {e}")
        raise

def analyze_output(stdout_data):

    for line in stdout_data.splitlines():
        if line.startswith('0x') and '"' in line:
            return line.split('"')[1]
    return None

def document_key(key_content):

    with open('rekordbox_db_pass.txt', 'w') as file:
        file.write(key_content)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            logging.error("Incorrect usage. Correct format: python script.py <path_to_application>")
            sys.exit(1)
        
        main_operation(sys.argv[1])
    except Exception as e:
        logging.error(f"An unexpected error occurred during execution: {e}")
        sys.exit(1)
