# Lessons on the Subprocess module
# Imports
import subprocess

if __name__ == "__main__":
    subprocess.run('ls')
    # Some commands require shell=True but it isn't recommended
    subprocess.run('dir', shell=True)
    # Alternate way to pass arguments
    subprocess.run(['ls', '-la'])

    # Capturing output of subprocesses
    p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
    print(p1.stdout, p1.stderr, p1.returncode)

    # An alternate way to do the same thing above is
    p2 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
    print(p2.stdout)

    # We can re direct stdout to other places also like a pipe
    with open('output.txt', 'w') as file:
        p3 = subprocess.run(['ls', '-la'], stdout=file, text=True)

    # Capturing and handling errors
    p_error = subprocess.run(['ls', '-la', 'wrong_dir'], capture_output=True, text=True)
    print(p_error.stdout, p_error.stderr, p_error.returncode)
    # We can handle errors by if conditions on return code

    # If we wanted the command itself to throw an error
    # p_error = subprocess.run(['ls', '-la', 'wrong_dir'], capture_output=True, check=True, text=True)
    # print(p_error.stdout)

    # Redirect errors to devnull
    p_error_redirect = subprocess.run(['ls', '-la', 'wrong_dir'], stderr=subprocess.DEVNULL)
    print(p_error_redirect.stderr)

    # Chaining commands
    p_chain = subprocess.run(['cat', 'test_file.txt'], capture_output=True)
    print(p_chain.stdout.decode())
    p_chain_2 = subprocess.run(['grep', '-n', 'simple'], capture_output=True, text=True, input=p_chain.stdout.decode())
    print(p_chain_2.stdout)

    # Alternately you could chain using pipes and shell=True
    p_chain_alt = subprocess.run('cat test_file.txt | grep -n simple', capture_output=True, text=True, shell=True)
    print(p_chain_alt.stdout)