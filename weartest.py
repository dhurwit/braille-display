import alternate
import readinput as ri
import sys
from multiprocessing import Process


def test(number_cycles, fsr_hertz, sol_hertz, sol_pin1, sol_pin2, filename = None):

    procs = []
      
    if not filename:
        filename = 'datalog.csv'
    
 
    procs.append(Process(target = ri.read_data, args = (
        fsr_hertz, sol_hertz, filename, number_cycles, )))
    procs.append(Process(target = alternate.sol_loop, args = (
        sol_pin1, sol_pin2, number_cycles, sol_hertz, )))

    return procs   
    

if __name__ == '__main__':
    cycles = input('How many cycles would you like to run? (in thousands): ')
    cycles = int(cycles * 1000)
    fsr_sample_rate = input ('Enter FSR sampling rate: ')
    solenoid_rate = input('Enter solenoid rate: ')
    sol_pin1 = input('Enter solenoid 1 pin number (on Raspberry Pi): ')
    sol_pin2 = input('Enter solenoid 2 pin number (on Raspberry Pi): ')
    filename = raw_input('Enter data filename (default: datalog.csv): ')
    
    procs = test(cycles, fsr_sample_rate, solenoid_rate, sol_pin1, sol_pin2, filename)
    map(lambda x: x.start(), procs)
    map(lambda x: x.join(), procs)

    sys.exit()
