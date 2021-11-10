class Filter:

	bad_word_list = ["shit", "crap", "fuck", "penguin"]

	def filter_new_joke(statement, punchline):
		bad_words = []

		if not statement or not punchline:
			return False

		else:
			joke = statement + " " + punchline
			for word in joke.lower().split(" "):
				if word in Filter.bad_word_list:
					bad_words.append(word)

		if len(bad_words) == 0:
			return True

		else:
			bad_words_str = ""
			prev_words = []
			for word in bad_words:
				if word in prev_words:
					pass
				elif bad_words.index(word) == 0:
					bad_words_str += word
				else:
					bad_words_str += ", " + word
				prev_words.append(word)
			return bad_words_str