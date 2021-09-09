func isLongPressedName(name string, typed string) bool {
	nameIndex, typedIndex := 0, 0

	for {
		if nameIndex >= len(name) && typedIndex >= len(typed) {
			return true
		} else if nameIndex >= len(name) || typedIndex >= len(typed) {
			return false
		} else if name[nameIndex] == typed[typedIndex] {
			nameDupNum, typedDupNum := deduplicate(name, nameIndex), deduplicate(typed, typedIndex)

			if nameDupNum > typedDupNum {
				return false
			} else {
				nameIndex += nameDupNum
				typedIndex += typedDupNum
			}
		} else {
			return false
		}
	}
}

func deduplicate(name string, index int) int {
	count := 1

	for i := index + 1; i < len(name); i++ {
		if name[index] != name[i] {
			break
		}

		count++
	}

	return count
}
