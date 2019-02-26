#! /usr/bin/env python3

''' Python script to convert a given NFA to the DFA '''

from collections import OrderedDict

#----------------------- Decorator for Exceptions--------------------------------------------
def safe_run(func):
    ''' Method decorator for handling exceptions '''
    def func_wrapper(*args, **kwargs):
        exit_statement = '(Press `Ctrl+C` to exit)'
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print('Invalid literal entered...\n{}\n'.format(exit_statement))
            except LessThanOne:
                print('Minimum one enitity required...\n{}\n'.format(exit_statement))
            except NotAlphaNumeric:
                print('Name should be alpha-numeric...\n{}\n'.format(exit_statement))
            except LengthExceeds:
                print('Name should be Max. 3 char long...\n{}\n'.format(exit_statement))
    return func_wrapper


#--------------------------- Custom Exceptions ---------------------------------------------
class LessThanOne(Exception):
    pass

class NotAlphaNumeric(Exception):
    pass

class LengthExceeds(Exception):
    pass


#------------------------- Finite Automata Class --------------------------------------------
class FiniteAutomata:
    ''' Class for defining the methods and storage schema of a Finite Automata '''
    
    # Constructor for initialising the tuples of the Finite Automata.
    def __init__(self):
        self.__states = self.__get_states()
        self.__inputs = self.__get_inputs()
        self.__final_states = self.__get_final_states()
        self.__start_state = self.__get_start_state()
        self.__transitions = self.__trans_func()

    #-------------------------------- Utility Methods ---------------------------------------
    @safe_run
    def __get_data(self, datatype):
        ''' Utility Method to get the data for various types of tuple of Finite Automata. '''
        data = OrderedDict()
        num = int(input('Enter the number of {}s in the Finite Automata: '.format(datatype)))
        if num < 1:
            raise LessThanOne
        print('Now, enter the name of the {}s (max 10 char)...'.format(datatype))
        for i in range(num):
            while True:
                temp = input('Enter name of {} {}: '.format(datatype, i+1))
                if not temp.isalnum():
                    raise NotAlphaNumeric
                if len(temp) > 10:
                    raise LengthExceeds
                if datatype == 'final state' and temp not in self.__states:
                    print('Entered state doesn\'t exists!!!\n')
                    continue
                break
            data[temp] = None
        return data

    def __get_states(self):
        ''' Utility Method to form the states tuple of the Finite Automata. '''
        return self.__get_data('state')
        
    def __get_inputs(self):
        ''' Utility Method to form the inputs tuple of the Finite Automata. '''
        print('\n')
        return self.__get_data('input')
    
    def __get_final_states(self):
        ''' Utility Method to form the final states tuple of the Finite Automata. '''
        print('\n')
        return self.__get_data('final state')

    def __get_start_state(self):
        ''' Utility Method to get the initial state of the Finite Automata. '''
        while True:
            state = input('\n\nEnter the initial state: ')
            if state in self.__states:
                break
            else:
                print('Entered state doesn\'t exists!!!\n')
        return state

    def __trans_func(self):
        ''' Utility Method to denote the transition function of the Finite Automata. '''
        transitions = OrderedDict((k,{}) for k in self.__states)
        for state in self.__states:
            print()
            if state == self.__start_state:
                print('\n\nEnter the transition for initial state: ')
            for input_ in self.__inputs:
                while True:
                    new_states = set(map(lambda x: x, input('Enter transition of {} for input {}: '.format(state, input_)).replace(',',' ').split()))
                    if all(state in self.__states for state in new_states):
                        break
                    else:
                        print('Entered state doesn\'t exist!!!\n')
                transitions[state][input_] = new_states if new_states != set() else '-'
        print()
        return transitions

    #--------------------------- Main Methods ---------------------------------------------
    def transition_table(self):
        ''' Method to show the transition table of the formed Finite Automata '''
        print('\nThe Transition table for the Finite Automata is: \n')
       
        print('State'.center(30), end='|')
        for inputs_ in self.__inputs:
            print('{}'.format(inputs_).center(30), end='|')
        print()

        for state in self.__states:
            if state == self.__start_state:
                print('-> {}'.format(state).center(30), end='|')
            else:
                print('   {}'.format(state).center(30), end='|')
            for input_ in self.__inputs:
                print('{}'.format(self.__transitions[state][input_]).center(30), end='|')
            print()
        print()

    def is_dfa(self):
        ''' Method to tell whether the formed Finite Automata is DFA or not. '''
        state_trans = [t for t in self.__transitions.values()]
        if any(len(trans.values()) > 1 for trans in state_trans):
            return False
        return True

    def convert_to_dfa(self):
        new_states_queue = [self.__start_state]
        new_transitions = OrderedDict()

        for state in new_states_queue:
            new_states_queue.remove(state)
            if '-' not in state:
                for trans_state in self.__transitions[state].values():
                    if '-'.join(trans_state) not in new_transitions:
                        new_states_queue.append('-'.join(trans_state))
            #    else:
            #        sub_states = state.split('-')
            #        state_values
            #        map(lambda s: self__transitions[s.values()], sub_states)

        print(new_transitions)

    def convert_to_mdfa():
        pass


#----------------------------- Main Method --------------------------------------
def main():
    ''' Main Driver Program '''

    print(''' 
     _____ _       _ _            _         _                        _        
    |  ___(_)_ __ (_) |_ ___     / \  _   _| |_ ___  _ __ ___   __ _| |_ __ _ 
    | |_  | | '_ \| | __/ _ \   / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _` |
    |  _| | | | | | | ||  __/  / ___ \ |_| | || (_) | | | | | | (_| | || (_| |
    |_|   |_|_| |_|_|\__\___| /_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\__,_|
    ''')

    while True:
        try:
            print('\n(Press `Ctrl+C` to exit)\nInitialising the Finite Automata...\n')
            fa = FiniteAutomata()

            while True:
                choice = input('''Main Menu:
                    1. Show the transition table of  FA
                    2. To check whether a FA is DFA or not
                    3. To convert a given FA into DFA
                    4. To convert a given FA into MDFA
                    5. Reset the FA
                    6. Exit\nEnter Your Choice: ''')
            
                if choice == '1':
                    fa.transition_table()
                elif choice == '2':
                    print('\n\nGiven Finite Automata is: {}\n\n'.format('DFA' if fa.is_dfa() else 'NFA'))
                elif choice == '3':
                    fa.convert_to_dfa()
                elif choice == '4':
                    pass
                elif choice == '5':
                    break
                elif choice == '6':
                    exit()
                else:
                    print('Invalid Choice!!!\n')
                
        except KeyboardInterrupt:
            print()
            exit()
    
if __name__ == '__main__':
    main()
