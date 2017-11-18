
import unittest

from binarysearchtree import BinarySearchTree

class Test_BinarySearchTree_IsEmpty(unittest.TestCase):
    def test_empty_tree( self ):
        bst = BinarySearchTree()
        self.assertEqual( bst.isEmpty(), True )

    def test_nonempty_tree( self ):
        bst = BinarySearchTree( 20 )
        self.assertEqual( bst.isEmpty(), False )


class Test_BinarySearchTree_Size(unittest.TestCase):
    def test_empty_tree( self ):
        bst = BinarySearchTree()
        self.assertEqual( bst.size(), 0 )

    def test_nonempty_tree( self ):
        bst = BinarySearchTree( 20 )
        self.assertEqual( bst.size(), 1 )



class Test_BinarySearchTree_Insert(unittest.TestCase):
    def test_insert_from_empty_tree( self ):
        bst = BinarySearchTree()
        self.assertEqual( bst.size(), 0 )
        bst.insert( 10 )
        self.assertEqual( bst.size(), 1 )

    def test_insert_from_nonempty_tree( self ):
        bst = BinarySearchTree( 10 )
        bst.insert( 20 )
        self.assertEqual( bst.size(), 2 )

    def test_insert_multiple_items_from_empty_tree( self ):
        bst = BinarySearchTree( )
        bst.insert( 20 )
        bst.insert( 10 )
        bst.insert( 30 )
        self.assertEqual( bst.size(), 3 )

    def test_insert_multiple_items_from_nonempty_tree( self ):
        bst = BinarySearchTree( 20 )
        bst.insert( 10 )
        bst.insert( 30 )
        bst.insert( 5 )
        self.assertEqual( bst.size(), 4 )

