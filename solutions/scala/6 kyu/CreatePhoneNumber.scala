//https://www.codewars.com/kata/525f50e3b73515a6db000b83/
object Kata {
  def createPhoneNumber(numbers: Seq[Int]): String = {
    return s"(${numbers.slice(0,3).mkString("")}) ${numbers.slice(4,7).mkString("")}-${numbers.slice(8,12).mkString("")}"
  }
}
