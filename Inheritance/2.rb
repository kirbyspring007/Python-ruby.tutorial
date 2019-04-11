class Cal
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+@v2
  end
  def subtract()
    return @v1-@v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
end
class CalMultiply < Cal
  def mutiply()
    return @v1*@v2
  end
end
class CalDivide < CalMultiply
  def divide()
    return @v1/@v2
  end
end
c1 = CalMultiply.new(10,10)
p c1.add()
p c1.mutiply()
c2 = CalDivide.new(20,10)
p c2, c2.add()
p c2, c2.mutiply
p c2, c2.divide
