import cv2  # Open Computer Vision
import numpy as np

# some standard colors
BLK=(0,0,0)
WHT=(255,255,255)
GRY=(100,100,100) # a little toward the darker side
# player colors
BLU=(255,0,0)     # Note OpenCV uses BGR not RGB
GRN=(0,255,0)
RED=(0,0,255)
YLW=(0,255,255)
BLUl=(255,128,128) # light versions (towards white)
GRNl=(128,255,128)
REDl=(128,128,255)
YLWl=(128,255,255)

# labels for piece sizes
SMA=1
MED=2
BIG=3


# The board has these positions
#     0   1   2
#     3   4   5
#     6   7   8
# Each position has concentric spots for SMA, MED, BIG pieces of any color
class OtrioArtist:
    def __init__(self, hw=500):
        self.nrows = hw # size of the board
        self.ncols = hw
        # start with an array of (0,0,0)=BLK
        self.img = np.zeros( (hw,hw,3), np.uint8)
        # math out from the board size what is the right placement
        # of the positions and the sizes of the donuts
        self.centers = []
        for ynum in (1,3,5):
            for xnum in (1,3,5):
                xc = int(xnum * (hw/6))
                yc = int(ynum * (hw/6))
                self.centers.append((xc, yc))
        # leave position [0] as a placeholder so you can index
        # like self.radii[MED] or whatever
        self.radii = [0,int(hw/3 * .09),int(hw/3 * .245), int(hw/3 * .40)]
        self.thick = [0,-5,7,7]
        self.new_board()

        # VideoWriter for animating successive board states as a video
        self.writer = None

    def draw_donut(self, xy, r, t, c):
        '''
        Draw a playing piece on the board as a donut (thicc circle)
        :param xy: Center coordinate, 2-tuple of integers
        :param r: Radius of center of donut thickness
        :param t: Thickness of drawing stroke (negative for filled)
        :param c: GRY, RED, GRN, RED, YLW, etc
        :return: None
        '''
        cv2.circle(self.img, xy, r, c, t) # note c/t switched order

    def draw_piece(self, which, color, where, add_frame=False):
        '''
        Draw a donut to indicate a piece being played
        :param which: Which size of piece? SMA,MED,BIG
        :param color: One of the player colors
        :param where: Position 0-8
        :param add_frame: whether to add the board state to a video in progress
        :return: None
        '''
        self.draw_donut(self.centers[where], self.radii[which],
                        self.thick[which], color)
        if add_frame:
            self.add_frame()


    def new_board(self):
        '''
        Starting with the black board, use draw_piece to draw
        grey donuts indicating all the empty spaces for pieces
        :return:
        '''
        for item in (SMA, MED, BIG):
            for i in range(9):
                self.draw_piece(item, GRY, i)

    def im_save(self, fname):
        '''
        Save image at each game state for visual aid for player
        :param fname: Filename for game state image
        :return:
        '''
        cv2.imwrite(fname, self.img)

    def start_video(self, fname, hertz=1):
        '''
        Start a new video file for animating a game (sequence of boards)
        :param fname: filename for the video, probably something.avi
        :param hertz: frames-per-second play rate
        :return: None
        '''
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        w_h = (self.ncols, self.nrows)
        self.writer = cv2.VideoWriter(fname, fourcc, hertz, w_h)

    def add_frame(self):
        '''
        Add the current board image as a frame to the video
        :return: None
        '''
        if self.writer is not None:
            self.writer.write(self.img)



if __name__ == '__main__':
    colors = [RED, GRN, BLU, YLW, REDl, GRNl, BLUl, YLWl]
    board = OtrioArtist()

    board.new_board()
    board.start_video('otrio.avi')
    board.add_frame()
    board.draw_piece(MED, RED, 4, True)
    board.draw_piece(SMA, BLU, 0, True)
    board.draw_piece(BIG, YLW, 7, True)
    board.draw_piece(SMA, GRN, 4, True)
    board.im_save('donuts.png')



