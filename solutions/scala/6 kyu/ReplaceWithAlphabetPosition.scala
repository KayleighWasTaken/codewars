//https://www.codewars.com/kata/546f922b54af40e1e90001da/
object Kata {

  def alphabetPosition(text: String): String = {
    text.toLowerCase.filter(_.isLetter).map(_ - 96).mkString(" ")
  }
}