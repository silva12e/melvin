import cmd
from bots.bot import MelvinBot

class CLI(cmd.Cmd):
    prompt = '> Enter query or enter exit() to quit: '
    
    def default(self, prompt):
        self.melvinBot = MelvinBot(
            model="text-davinci-003",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6
        )
        print("Melvin begins thinking...")
        completion_text = (f"{self.melvinBot.completions(prompt)}")


    def do_q(self, line):
        exit();

if __name__ == '__main__':
    CLI().cmdloop()
