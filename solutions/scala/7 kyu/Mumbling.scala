//https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/
object Codewars {
  def accum(s: String): String = {
    s.indices.map(i => (s(i).toLower.toString * (i + 1)).capitalize).mkString("-")
  }
}