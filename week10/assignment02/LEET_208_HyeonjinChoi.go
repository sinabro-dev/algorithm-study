type Trie struct {
	data []string
}

func Constructor() Trie {
	return Trie{}
}

func (this *Trie) Insert(word string) {
	this.data = append(this.data, word)
}

func (this *Trie) Search(word string) bool {
	for _, data := range this.data {
		if data == word {
			return true
		}
	}

	return false
}

func (this *Trie) StartsWith(prefix string) bool {
	for _, data := range this.data {
		if len(data) >= len(prefix) && data[:len(prefix)] == prefix {
			return true
		}
	}

	return false
}
