class Player
  attr_reader :health
  attr_accessor :name

  def initialize(name, health = 100)
    @name = name.capitalize
    @health = health
  end

  def score
    @health + @name.length
  end

  def to_s
    "I'm #{@name} with a health of #{@health} and a score of #{score}"
  end

  def boost
    @health += 15
  end

  def drain
    @health -= 10
  end
end

player_4 = Player.new("finn", 60)

number_rolled = rand(1..6)

case number_rolled
when 1..2
  player_4.drain
  puts "#{player_4.name} got drained 😩"
when 3..4
  puts "#{player_4.name} got skipped"
else
  player_4.boost
  puts "#{player_4.name} got boosted 😁"
end
