//https://www.codewars.com/kata/575fa9afee048b293e000287/
object Sol {
  def howMuchWater(water: Int, maxLoad: Int, clothes: Int): Either[Double, String] = {
    if (clothes > maxLoad * 2) {
      Right("Too much clothes")
    } else if (clothes < maxLoad) {
      Right("Not enough clothes")
    } else {
      val waterUsed = water * math.pow(1.1, clothes - maxLoad)
      Left(f"$waterUsed%1.2f".toDouble)
    }
  }
}
