//https://www.codewars.com/kata/5264d2b162488dc400000001/
object Codewars {
  def spinWords(sentence: String): String = {
    sentence.split(" ").map(s => if (s.size >= 5) {s.reverse} else {s}).mkString(" ")
  }
}