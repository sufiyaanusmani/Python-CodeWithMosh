class TagCloud:
    def __init__(self):
        self.__tags = {}     # __tags makes it private

    
    def add(self, tag):
        tag = tag.lower()
        self.__tags[tag] = self.__tags.get(tag, 0) + 1


    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)


    def __setitem__(self, tag, value):
        self.__tags[tag.lower()] = value


    def __len__(self):
        return len(self.__tags)


    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
print(cloud.__tags)