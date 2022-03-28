class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.sigma = self.states = []
        self.transitions = []
        self.start = ''
        self.final = []
        self.Error = set()
        with open(config_file, 'r') as file:
            lines = file.readlines()
        readComponent = ''
        for line in lines:
            line = line.strip()
            if line[0] == '#':
                continue;
            sep = ".,:?!;"
            for semn in sep:
                line = line.replace(semn, ' ')
            line = line.split()
            if line[0].lower() == 'sigma':
                readComponent = 'sigma'
            elif line[0].lower() == 'states':
                readComponent = 'states'
            elif line[0].lower() == 'transitions':
                readComponent = 'transitions'
            elif line[0].lower() == 'end':
                readComponent = ''
            elif readComponent == 'sigma':
                self.sigma.append(line[0])
            elif readComponent == 'states':
                self.states.append(line[0])
                if 'S' in line or 's' in line:
                    if self.start != '':
                        self.Error.add("Too many start nodes")
                    self.start = line[0]
                if 'F' in line or 'f' in line:
                    self.final.append(line[0])
            elif readComponent == 'transitions':
                self.transitions.append(tuple(line))
        for error in self.Error:
            print(error)
        if len(self.Error) == 0:
            print("Automatul a fost citit cu succes")

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        for transition in self.transitions:
            if len(transition) != 3:
                return "Not all transitions have 3 elements"
            if transition[0] not in self.states or transition[2] not in self.states:
                return "Some transitions don't have valid states"
            if transition[1] not in self.sigma:
                return "Sigma is not recognized for some transitions"

        return "automaton validat cu succes"

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        pass
    

if __name__ == "__main__":
    a = Automaton('../config.in')
    print(a.validate())
