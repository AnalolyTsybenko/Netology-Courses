pattern_name = r'\W+'
pattern_phone = r'(\+7|8)[\s(]{0,3}(\d{3})[\s)-]{0,3}(\d{3})[-\s]{0,3}(\d{2})[-\s]{0,3}(\d{2})[\s(]{0,3}(доб\.)?\s?(\d+)?[\s)]?'
substitution_phone = r'+7(\2)\3-\4-\5 \6\7'
