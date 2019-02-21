#! /usr/bin/env python3

''' Python script to convert a given NFA to the DFA '''

from collections import OrderedDict

def safe_run(func):
    def func_wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print('Invalid literal entered...\n(Press `Ctrl+C` to exit)\n')
            except Exception:
                print('Name should be alpha-numeric...\n(Press `Ctrl+C` to exit)\n')
    return func_wrapper

class FiniteAutomata:

    def __init__(self):
        self.__states = self.__get_states()
        self.__inputs = self.__get_inputs()
        self.__final_states = self.__get_final_states()
        self.__start_state = self.__get_start_state()
        self.__transitions = self.__trans_func()

    @safe_run
    def __get_data(self, datatype):
        data = OrderedDict()
        num = int(input('Enter the number of {}s in the Finite Automata: '.format(datatype)))
        print('\nNow, enter the name of the {}s (max 3 char)...\n'.format(datatype))
        for i in range(num):
            while True:
                temp = input('Enter name of {} {}: '.format(datatype, i+1))
                if not temp.isalnum():
                    raise Exception
                if datatype == 'final state' and temp not in self.__states:
                    print('Entered state doesn\'t exists!!!\n')
                    continue
                break
            data[temp] = None
        return data

    def __get_states(self):
        return self.__get_data('state')
        
    def __get_inputs(self):
        print('\n')
        return self.__get_data('input')
    
    def __get_final_states(self):
        print('\n')
        return self.__get_data('final state')

    def __get_start_state(self):
        while True:
            state = input('\n\nEnter the initial state: ')
            if state in self.__states:
                break
            else:
                print('Entered state doesn\'t exists!!!\n')
        return state

    def __trans_func(self):
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
                transitions['{}'.format(state)]['{}'.format(input_)] = new_states
        return transitions

    def is_dfa(self):
        state_trans = [t for t in self.__transitions.values()]
        if any(len(trans.values()) > 1 for trans in state_trans):
            return False
        return True

    def convert_to_dfa():
        pass
    
    def convert_to_mdfa():
        pass

def main():
    ''' Main Driver Program '''

    print(''' 
     _____ _       _ _            _         _                        _        
    |  ___(_)_ __ (_) |_ ___     / \  _   _| |_ ___  _ __ ___   __ _| |_ __ _ 
    | |_  | | '_ \| | __/ _ \   / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _` |
    |  _| | | | | | | ||  __/  / ___ \ |_| | || (_) | | | | | | (_| | || (_| |
    |_|   |_|_| |_|_|\__\___| /_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\__,_|
    ''')

    options = ['1', '2', '3', '4']
    
    while True:
        try:
                
            choice = input('''
            Main Menu:
                    1. To check whether a FA is DFA or not
                    2. To convert a given FA into DFA
                    3. To convert a given FA into MDFA
                    4. Exit
            Enter Your Choice: ''')
            
            if choice not in options:
                print('Invalid Choice!!!\n(Press `Ctrl+C` to exit)\n')
                continue

            elif choice == '4':
                exit()

            fa = FiniteAutomata()
            if choice == '1':
                print('\n\nGiven Finite Automata is: {}\n\n'.format('DFA' if fa.is_dfa() else 'NFA'))
            elif choice == '2':
                pass
            else:
                pass
                
        except KeyboardInterrupt:
            exit()
    

if __name__ == '__main__':
    main()