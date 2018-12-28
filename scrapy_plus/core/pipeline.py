
class Pipeline(object):

  def process_item(self, item, spider):

      print(item.data)
      # print(123)

      return item
