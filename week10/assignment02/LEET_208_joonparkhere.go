package main

var (
	dummy = byte(0)
	last = byte(1)
)

type Trie struct {
	value byte
	children []*Trie
}

// Constructor Initialize your data structure here. */
func Constructor() Trie {
	return Trie{
		value: dummy,
		children: make([]*Trie, 0),
	}
}

// Insert Inserts a word into the trie. */
func (t *Trie) Insert(word string)  {
	idx := 0
	cur := t

	for ; idx < len(word); idx++ {
		flag := uint8(0)
		for _, child := range cur.children {
			if child.value == word[idx] {
				flag = uint8(1)
				cur = child
				break
			}
		}
		if flag == 0 {
			break
		}
	}

	for ; idx < len(word); idx++ {
		node := &Trie{
			value: word[idx],
			children: make([]*Trie, 0),
		}
		cur.children = append(cur.children, node)
		cur = node
	}

	end := &Trie{
		value: last,
		children: make([]*Trie, 0),
	}
	cur.children = append(cur.children, end)
}

func (t *Trie) find(str string) (bool, int) {
	cur := t

	for _, c := range []byte(str) {
		flag := uint8(0)
		for _, child := range cur.children {
			if child.value == c {
				flag = uint8(1)
				cur = child
				break
			}
		}
		if flag == 0 {
			return false, 0
		}
	}

	for _, child := range cur.children {
		if child.value == last {
			return true, 0
		}
	}
	return true, len(cur.children)
}

// Search Returns if the word is in the trie. */
func (t *Trie) Search(word string) bool {
	ok, childrenSize := t.find(word)
	if !ok {
		return false
	} else if childrenSize > 0 {
		return false
	} else {
		return true
	}
}

// StartsWith Returns if there is any word in the trie that starts with the given prefix. */
func (t *Trie) StartsWith(prefix string) bool {
	ok, _ := t.find(prefix)
	return ok
}
