
Score = {}

function Score:load()
    self.font = love.graphics.newFont("assets/Pixeled.ttf", 50)
    self.score = 0
    self.x = love.graphics.getWidth() / 2
    self.y = 10
    self.scored = love.audio.newSource("assets/bing2.mp3", "static")
    self.scored:setVolume(0.5)
end

function Score:update(dt)
    self:playerScores()
end

function Score:draw()
    xAdjustment = self.font:getWidth(self.score) / 2
    love.graphics.print({{0, 0, 0, 1}, self.score}, self.font, self.x - xAdjustment + 3, self.y + 3)
    love.graphics.print(self.score, self.font, self.x - xAdjustment, self.y)
end

function Score:playScoredEffect()
    local pitch = math.min(3, 0.5 + self.score * 0.05)
    self.scored:setPitch(pitch)
    self.scored:play()
end

function Score:playerScores()
    for i, obstacle in ipairs(obstacles.obstacles) do
        if not obstacle.wasSeen and obstacle.top.x <= Player.x then
            self:playScoredEffect()
            obstacle.wasSeen = true
            self.score = self.score + 1
        end
    end
end