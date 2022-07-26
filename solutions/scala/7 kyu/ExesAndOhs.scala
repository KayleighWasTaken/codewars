//https://www.codewars.com/kata/55908aad6620c066bc00002a/
object ExesAndOhs {

  def xo(str: String): Boolean = {
    str.toLowerCase.count(_ == 'x') == str.toLowerCase.count(_ == 'o')
  }
}