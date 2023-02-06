import cmd

class CLI(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = '> '
    
    def do_greet(self, line):
        """Greet the user."""
        name = line.strip()
        print("Hello, " + name + "!")
        
    def do_exit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    CLI().cmdloop()