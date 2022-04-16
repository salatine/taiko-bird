MenuState = GameState:new()

function MenuState:update(dt)
    Background:update(dt)
    Menu:update(dt)
    AI:update(dt)
end

function MenuState:draw()
    Menu:draw()
    Coins:draw()
    AI:draw()
end

function MenuState:onMousePressed(mousePosition)
    if Menu.playButton:isHovered(mousePosition) then
        Menu.playButton:setButtonAsPressed()
    end

    if Menu.rateButton:isHovered(mousePosition) then
        Menu.rateButton:setButtonAsPressed()
    end

    if Menu.colorsButton:isHovered(mousePosition) then
        Menu.colorsButton:setButtonAsPressed()
    end
    
    if Menu.shopButton:isHovered(mousePosition) then
        Menu.shopButton:setButtonAsPressed()
    end
end

function MenuState:onMouseReleased(mousePosition)
    Menu.playButton:onHovered(mousePosition, function() Menu:playGame() end)
    Menu.rateButton:onHovered(mousePosition, function() Credits:showCredits() end) -- Menu:rateGame
    Menu.colorsButton:onHovered(mousePosition, function() gameState = ColorsState end)
    Menu.shopButton:onHovered(mousePosition, function() Menu:openStore() end)
    Menu:onMouseReleased()
end

function MenuState:onFocus(focus)
    
end