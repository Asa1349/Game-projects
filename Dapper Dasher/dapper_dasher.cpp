/* 
-----------------------------------------------------------------------------
File name: dapper_dasher.cpp
Version: 1.0
Description: 
Author: AP
Date of last modification: 13.02.2024
----------------------------------------------------------------------------- 
*/

// libraries used -----------------------------------------------------------

#include "raylib.h"


// Declaration of Functions an Structures -----------------------------------

struct AnimationData
    {
        Rectangle rec;
        Vector2 pos;
        int frame;
        // amount of time before the animation playerFrame gets updated
        float updateTime;
        float runningTime;
    };


bool isOnGround(AnimationData data, int windowHeight)
    {
        return data.pos.y >= windowHeight - data.rec.height;
    };


AnimationData updateAnimData(AnimationData data, float deltaTime, int maxFrame)
    {
        // each frame, deltaTime gets added to runningTime
        data.runningTime += deltaTime;
        // if runningTime reaches 1/xx sec, it gets reseted and the animation gets updated
        if (data.runningTime >= data.updateTime) 
            {
                data.runningTime = 0.0;
                data.rec.x = data.frame * data.rec.width;
                data.frame ++;
                if (data.frame > maxFrame) {data.frame = 0;}
            }
        return data;
    };


// main function ------------------------------------------------------------
int main()
{
    SetTargetFPS(60);

    // window dimensions
    const int windWidth{512};
    const int winHeight{380};
    InitWindow(windWidth , winHeight, "Dapper Dasher");


    // Player
    Texture2D player = LoadTexture("textures/scarfy.png");
    AnimationData playerData{
                            {0.0, 0.0, (float)player.width/6, (float)player.height}, // Rectangle rec
                            {windWidth/2 - playerData.rec.width/2, winHeight - playerData.rec.height}, // Vector2 pos
                            {0}, // int frame
                            {1.0/10.0}, // float updateTime
                            {0.0} // float runningTime
                            };

    int playerVelocity{0};
    bool inAir{false};
    // accelaration due to gravity (pixels/sec)/sec - movement indipendent from framerate
    const int gravity{1500};
    const int jumpVelocity{-800};


    // Nebula
    Texture2D nebula = LoadTexture("textures/12_nebula_spritesheet.png");
    const int sizeOfNebulae{GetRandomValue(6, 15)};
    AnimationData nebulae[sizeOfNebulae]{};

    for (int i = 0; i < sizeOfNebulae; i++)
        {
            nebulae[i].rec.x = 0.0;
            nebulae[i].rec.y = 0.0;
            nebulae[i].rec.width = (float)nebula.width/8;
            nebulae[i].rec.height = (float)nebula.height/8;
            nebulae[i].pos.x = windWidth + i * GetRandomValue(500,700);
            nebulae[i].pos.y = winHeight - (float)nebula.height/8;            
            nebulae[i].frame = 0;
            nebulae[i].updateTime = 1.0/100.0;
            nebulae[i].runningTime = 0.0;
        };

    int nebulaVelocity{-230};


    // Background
    Texture2D background = LoadTexture("textures/far-buildings.png");
    Texture2D midground = LoadTexture("textures/back-buildings.png");
    Texture2D foreground = LoadTexture("textures/foreground.png");
    float bgPosX{0};
    float mgPosX{0};
    float fgPosX{0};
    

    int score{0};
    bool nebulaScored[sizeOfNebulae] = {false};
    int nebulaeExitedScreen{};
    bool collision{};


    // Game Loop ------------------------------------------------------------

    while (!WindowShouldClose())
    {
        // deltatime (time since last playerFrame)
        const float deltaTime{GetFrameTime()};
        
        BeginDrawing();
        ClearBackground(BLACK);

        // draw background
        Vector2 bg1Pos{bgPosX, 0.0};
        Vector2 bg2Pos{bgPosX + background.width * 2, 0.0};
        Vector2 mg1Pos{mgPosX, 0.0};
        Vector2 mg2Pos{mgPosX + midground.width * 2, 0.0};
        Vector2 fg1Pos{fgPosX, 0.0};
        Vector2 fg2Pos{fgPosX + foreground.width * 2, 0.0};
        DrawTextureEx(background, bg1Pos, 0.0, 2.0, WHITE);
        DrawTextureEx(background, bg2Pos, 0.0, 2.0, WHITE);
        DrawTextureEx(midground, mg1Pos, 0.0, 2.0, WHITE);
        DrawTextureEx(midground, mg2Pos, 0.0, 2.0, WHITE);
        DrawTextureEx(foreground, fg1Pos, 0.0, 2.0, WHITE);
        DrawTextureEx(foreground, fg2Pos, 0.0, 2.0, WHITE);

        // scroll background
        bgPosX -= 20 * deltaTime;
        mgPosX -= 40 * deltaTime;
        fgPosX -= 80 * deltaTime;
        if (bgPosX <= -background.width * 2){bgPosX = 0.0;}
        if (mgPosX <= -midground.width * 2){mgPosX = 0.0;}
        if (fgPosX <= -foreground.width * 2){fgPosX = 0.0;}

        

        
        // checks for collision
        for (AnimationData nebula : nebulae)
            {
                // more accurate hitbox
                float pad{50};
                Rectangle nebRec{nebula.pos.x + pad, nebula.pos.y + pad, nebula.rec.width - pad * 2, nebula.rec.height - pad * 2};
                Rectangle playerRec{playerData.pos.x, playerData.pos.y, playerData.rec.width, playerData.rec.height};
                if (CheckCollisionRecs(nebRec, playerRec))
                    {
                        collision = true;
                    };
            }


        // update score
        for (int i = 0; i < sizeOfNebulae; i++) 
            {
                if (nebulae[i].pos.x + nebulae[i].rec.width < 0 && !nebulaScored[i]) 
                    {
                        score++;
                        nebulaScored[i] = true; 
                        nebulaeExitedScreen++;
                    }
            }


        if (collision)
            {
                // lose game
                DrawText("GAME OVER!", windWidth/4, winHeight/2, 40, RED);
                DrawText(TextFormat("SCORE: %i", score), 10, 10, 20,BLACK);
            }
        
        else if (nebulaeExitedScreen == sizeOfNebulae)
            {
                // win game
                  DrawText("YOU WIN!", windWidth/4 + 40, winHeight/2, 40, GREEN);
                  DrawText(TextFormat("SCORE: %i", score), 10, 10, 20,BLACK);
            }
        
        else
            {
                // Draw Player
                DrawTextureRec(player, playerData.rec, playerData.pos, WHITE);
                // Draw Nebula
                for (int i = 0; i < sizeOfNebulae; i++)
                    {
                        DrawTextureRec(nebula,nebulae[i].rec, nebulae[i].pos, WHITE);
                    }
           
                // check player position
                if (isOnGround(playerData, winHeight))
                    {inAir = false;
                    playerVelocity = 0;}
                else 
                    {inAir = true;
                    // apply gravity
                    playerVelocity += gravity * deltaTime;}
                // Player jump
                if (IsKeyPressed(KEY_SPACE) && !inAir) 
                    {playerVelocity += jumpVelocity;}
                // update Player position
                playerData.pos.y += playerVelocity * deltaTime;
                // update Player animation frame
                if (!inAir)
                    {
                        playerData = updateAnimData(playerData, deltaTime, 5);
                    }

                // update Nebula position
                for (int i = 0; i < sizeOfNebulae; i++)
                    {
                        nebulae[i].pos.x += nebulaVelocity * deltaTime;
                    }
                // update Nebula animation Frame
                for (int i = 0; i < sizeOfNebulae; i++)
                    {   
                        nebulae[i] = updateAnimData(nebulae[i], deltaTime, 7);
                    }
            }


        EndDrawing();
    }

    UnloadTexture(player);
    UnloadTexture(nebula);
    UnloadTexture(background);
    UnloadTexture(midground);
    UnloadTexture(foreground);

    CloseWindow();
}
