#main loop
    #pir로 탑승감지
    # if 사람이 타면
        # 사용 설명, 
#네비 loop 실행
    #1. 목적지 입력
    #loop
        #2. 현재 위치를 파악한다
        #3. 최단경로를 계산한다. =계산된 경로: A-B-C-D, c는 코너이고, D는 c를 바라봤을때 우회전이다.
            #loop
            #4 진동, 음성 피드백
                #if 현재 노드가 코너일 때 =C 코너인지 아닌지 4가지 중 하나라면,

                    #######1. 다음 노드D 로 우회전인지 좌회전인지 직진인지 하드코딩

                    ########2. 각 노드에 주어진 값에 따라 라디안 값을 임의로 0, 90, 180, 270 넣고
                    ######## 차이가 -90인지 +90인지 / -270 인지 +270 에 따라 우회전 좌회전 판별

                    #if 다음노드로 직진이면
                        #(NONE)
                    #elif 다음노드로 우회전이면 (=다음 비콘을 바라봤을 때 각도 데이터가 (90)도 이상 크게 차이나면...)
                        #TTS: 우회전입니다.

                        ######  a<b<c == a<b and b<c
                        #while(사용자가 바라보는 각도 +90 -5 <= 사용자가 바라보는 각도
                        #      and 사용자가 바라보는 각도 <= 사용자가 바라보는 각도 +90 +5
                        #                       or
                        #      사용자가 바라보는 각도 -270 +5(오차) <= 사용자가 바라보는 각도
                        #      and 사용자가 바라보는 각도 <= 사용자가 바라보는 각도 -270 +5)

                            # 진동 : 우측

                    #elif 다음노드로 죄화전이면
                        #위 분기와 같이 계산
                     
                    #elif 방향 전환이 필요한 노드 (대각선 이동) 이면
                        #TTS: 진동 피드백에 따라 방향을 전환해주세요.
                        
                #5.3에서 계산된 경로를 따라가는지 계속확인
                # if목적지에 도착 하면
                    #목적도착 기능
                # if잘따라가면 (= 계산된 경로: A-B-C-D
                                #현재노드 A, 다음노드 B, 다다음 노드 C,->
                                # 현재노드 B, 다음노드 C, 다다음 노드 D )
                #elif 잘 못따라가면
                    # (break)
            
