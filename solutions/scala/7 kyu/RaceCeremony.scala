//https://www.codewars.com/kata/62cecd4e5487c10028996e04/
object Sol{
  def racePodium(blocks: Int): (Int, Int, Int) = {
    if (blocks == 7) {
      (2, 4, 1)
    } else {
      val s = (blocks + 2) / 3
      (s, s + 1, blocks - 2 * s - 1)
    }
  }
}