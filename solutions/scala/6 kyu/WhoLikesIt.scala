//https://www.codewars.com/kata/5266876b8f4bf2da9b000362/
object Sol {
  def likes(names: Array[String]): String = {
    names.length match
    case 0 => "no one likes this"
    case 1 => "%s likes this".format(names(0))
    case 2 => "%s and %s like this".format(names: _*)
    case 3 => "%s, %s and %s like this".format(names: _*)
    case _ => "%s, %s and %s others like this".format(names(0), names(1), names.length - 2)
  }
}