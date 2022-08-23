import java.util.Arrays;

public class ColorringBook {
    static int sizeOfArea = 0;
    static int oriVal = 0;
    static int[][] _picture;

    public int[] solution(int m, int n, int[][] picture) {

        int[] answer = new int[2];
        int numberOfArea = 0;
        int maxSize = 0;
        _picture = new int[m][n];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                _picture[i][j] = picture[i][j];
            }
        }
        // 탐색을 마친 공간은 -1로 변경
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // -1은 이미 지나간 자리 0은 빈 공간
                if (_picture[i][j] != -1 && _picture[i][j] != 0)
                {
                    numberOfArea++;
                    oriVal = _picture[i][j];
                    _picture[i][j] = -1;
                    sizeOfArea++;
                    getSizeOfArea(i, j, _picture);
                    if(sizeOfArea > maxSize) maxSize = sizeOfArea;

                }
                sizeOfArea = 0;
            }
        }
        return new int[]{numberOfArea, maxSize};
    }
    public void getSizeOfArea(int i, int j, int[][] picture)
    {
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, 1, -1, 0};
        // 4면 탐색
        for(int ii = 0; ii < 4; ii++) {
            int nx = i + dx[ii];
            int ny = j + dy[ii];
            if (0 <= nx && nx < picture.length && 0 <= ny && ny < picture[0].length) {
                if (oriVal == picture[nx][ny]) {
                    sizeOfArea++;
                    picture[nx][ny] = -1;
                    getSizeOfArea(nx, ny, picture);
                }
            }
        }
    }

    public static void main(String[] args) {
        int m = 6;
        int n = 4;
        int[][] picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};

        ColorringBook c = new ColorringBook();
        int[] ans = c.solution(m, n, picture);
        System.out.println(ans[0] + ":" + ans[1]);
    }
}
