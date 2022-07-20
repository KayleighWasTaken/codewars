//https://www.codewars.com/kata/54ff3102c1bad923760001f3/
object Sol {

  def getCount(inputStr: String): Int = {
    inputStr.filter(c => "aeiou" contains c).length
  }
}