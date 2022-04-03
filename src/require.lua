function requireAll()
    require("src/utils")
    require("src/background")
    require("src/obstacles")
    require("src/obstacle")
    require("src/pipe")
    require("src/player")
    require("src/score")
    require("src/save")
    require("src/gameover")
    require("src/menu")
    require("src/ai")
    require("src/pause")
    require("src/credits")
    require("src/colors")
    require("src/aicolors")
    require("src/components/button")
    require("src/shaders")
    require("src/components/colorbutton")
    require("src/audio/ShepardToneSource")
    shapes = require("libraries.HC.shapes")
    binser = require("libraries.binser")

    if utils.isMobile then
        admob = require('admob')
    else
        admob = require('src/polyfills/admob')
    end
end

requireAll()