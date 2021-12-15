#Quene lab by Zion Choi
#12/15/2021
from quene_node import quene_node as qn
from quene import quene

if __name__ == '__main__':
    #creating test nodes
    test_node1 = qn(1)
    test_node2 = qn(2)
    test_node3 = qn(3)

    #test 1 checks enquene for first node
    #and quene size
    print('Test 1')
    test_quene = quene()
    test_quene.enquene(test_node1)
    print('Top Node: ('+test_quene.peek().toString()+')')
    print('Current size: '+str(test_quene.size()))

    #test 2 tests dequene and size again
    print('\nTest 2')
    print(test_quene.dequene().toString())
    print('Current size: '+str(test_quene.size()))

    #test 3 tests quene with multiple nodes
    print('\nTest 3')
    test_quene.enquene(test_node2)
    test_quene.enquene(test_node3)
    print('Top Node: ('+test_quene.peek().toString()+')')
    print('Dequened: '+test_quene.dequene().toString())
    print('Top Node: ('+test_quene.peek().toString()+')')