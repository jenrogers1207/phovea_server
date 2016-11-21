###############################################################################
# Caleydo - Visualization for Molecular Biology - http://caleydo.org
# Copyright (c) The Caleydo Team. All rights reserved.
# Licensed under the new BSD license,  available at http://caleydo.org/license
###############################################################################


def _mix(a, b, alpha):
  if isinstance(a, tuple):
    return tuple([_mix(ai, bi, alpha) for ai, bi in zip(a, b)])
  return int(a * (1 - alpha) + b * alpha)


class ColorPalette(object):
  def __init__(self, *colors):
    self._colors = colors

  def as_palette(self):
    l = len(self._colors)
    if l == 256:
      return [(r, g, b) for r, g, b, a in self._colors]
    if l == 1:
      return self._colors * 256  # repeat the same color for the full range
    elif l == 2:
      a = self._colors[0]
      b = self._colors[1]
      return [_mix(a, b, i / 256.) for i in xrange(256)]
    elif l == 3:
      a = self._colors[0]
      center = self._colors[1]
      b = self._colors[2]
      center_a = _mix(a, center, 127.5 / 128)
      center_b = _mix(center, b, 0.5 / 128)
      return [_mix(a, center_a, i / 128.) for i in xrange(128)] + [_mix(center_b, b, i / 128.) for i in xrange(128)]
    return None  # not yet done


class ColorPaletteFix(object):
  def __init__(self, colors):
    self._colors = [(r, g, b) for r, g, b, a in colors]

  def as_palette(self):
      return self._colors

neutral_grey = (220, 220, 220)
blue_white_red = ColorPaletteFix([(5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (5, 113, 176, 255), (7, 114, 176, 255), (9, 115, 177, 255), (12, 116, 177, 255), (14, 117, 178, 255), (16, 119, 178, 255), (18, 120, 179, 255), (21, 121, 179, 255), (23, 122, 180, 255), (25, 123, 180, 255), (27, 124, 181, 255), (30, 125, 181, 255), (32, 126, 182, 255), (34, 127, 182, 255), (36, 129, 182, 255), (39, 130, 183, 255), (41, 131, 183, 255), (43, 132, 184, 255), (45, 133, 184, 255), (48, 134, 185, 255), (50, 135, 185, 255), (52, 136, 186, 255), (54, 138, 186, 255), (57, 139, 187, 255), (59, 140, 187, 255), (61, 141, 187, 255), (63, 142, 188, 255), (65, 143, 188, 255), (68, 144, 189, 255), (70, 145, 189, 255), (72, 146, 190, 255), (74, 148, 190, 255), (77, 149, 191, 255), (79, 150, 191, 255), (81, 151, 192, 255), (83, 152, 192, 255), (86, 153, 193, 255), (88, 154, 193, 255), (90, 155, 193, 255), (92, 156, 194, 255), (95, 158, 194, 255), (97, 159, 195, 255), (99, 160, 195, 255), (101, 161, 196, 255), (104, 162, 196, 255), (106, 163, 197, 255), (108, 164, 197, 255), (110, 165, 198, 255), (113, 167, 198, 255), (115, 168, 198, 255), (117, 169, 199, 255), (119, 170, 199, 255), (121, 171, 200, 255), (124, 172, 200, 255), (126, 173, 201, 255), (128, 174, 201, 255), (130, 175, 202, 255), (133, 177, 202, 255), (135, 178, 203, 255), (137, 179, 203, 255), (139, 180, 204, 255), (142, 181, 204, 255), (144, 182, 204, 255), (146, 183, 205, 255), (148, 184, 205, 255), (151, 185, 206, 255), (153, 187, 206, 255), (155, 188, 207, 255), (157, 189, 207, 255), (160, 190, 208, 255), (162, 191, 208, 255), (164, 192, 209, 255), (166, 193, 209, 255), (168, 194, 209, 255), (171, 195, 210, 255), (173, 197, 210, 255), (175, 198, 211, 255), (177, 199, 211, 255), (180, 200, 212, 255), (182, 201, 212, 255), (184, 202, 213, 255), (186, 203, 213, 255), (189, 204, 214, 255), (191, 206, 214, 255), (193, 207, 215, 255), (195, 208, 215, 255), (198, 209, 215, 255), (200, 210, 216, 255), (202, 211, 216, 255), (204, 212, 217, 255), (207, 213, 217, 255), (209, 214, 218, 255), (211, 216, 218, 255), (213, 217, 219, 255), (216, 218, 219, 255), (218, 219, 220, 255), (220, 220, 220, 255), (220, 218, 218, 255), (220, 215, 216, 255), (219, 213, 214, 255), (219, 211, 212, 255), (219, 209, 210, 255), (219, 206, 208, 255), (219, 204, 206, 255), (219, 202, 204, 255), (218, 199, 202, 255), (218, 197, 200, 255), (218, 195, 198, 255), (218, 193, 197, 255), (218, 190, 195, 255), (217, 188, 193, 255), (217, 186, 191, 255), (217, 183, 189, 255), (217, 181, 187, 255), (217, 179, 185, 255), (216, 176, 183, 255), (216, 174, 181, 255), (216, 172, 179, 255), (216, 170, 177, 255), (216, 167, 175, 255), (216, 165, 173, 255), (215, 163, 171, 255), (215, 160, 169, 255), (215, 158, 167, 255), (215, 156, 165, 255), (215, 154, 163, 255), (214, 151, 161, 255), (214, 149, 159, 255), (214, 147, 157, 255), (214, 144, 155, 255), (214, 142, 153, 255), (213, 140, 151, 255), (213, 138, 150, 255), (213, 135, 148, 255), (213, 133, 146, 255), (213, 131, 144, 255), (213, 128, 142, 255), (212, 126, 140, 255), (212, 124, 138, 255), (212, 121, 136, 255), (212, 119, 134, 255), (212, 117, 132, 255), (211, 115, 130, 255), (211, 112, 128, 255), (211, 110, 126, 255), (211, 108, 124, 255), (211, 105, 122, 255), (210, 103, 120, 255), (210, 101, 118, 255), (210, 99, 116, 255), (210, 96, 114, 255), (210, 94, 112, 255), (210, 92, 110, 255), (209, 89, 108, 255), (209, 87, 106, 255), (209, 85, 104, 255), (209, 83, 103, 255), (209, 80, 101, 255), (208, 78, 99, 255), (208, 76, 97, 255), (208, 73, 95, 255), (208, 71, 93, 255), (208, 69, 91, 255), (207, 66, 89, 255), (207, 64, 87, 255), (207, 62, 85, 255), (207, 60, 83, 255), (207, 57, 81, 255), (207, 55, 79, 255), (206, 53, 77, 255), (206, 50, 75, 255), (206, 48, 73, 255), (206, 46, 71, 255), (206, 44, 69, 255), (205, 41, 67, 255), (205, 39, 65, 255), (205, 37, 63, 255), (205, 34, 61, 255), (205, 32, 59, 255), (204, 30, 57, 255), (204, 28, 56, 255), (204, 25, 54, 255), (204, 23, 52, 255), (204, 21, 50, 255), (204, 18, 48, 255), (203, 16, 46, 255), (203, 14, 44, 255), (203, 11, 42, 255), (203, 9, 40, 255), (203, 7, 38, 255), (202, 5, 36, 255), (202, 2, 34, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255), (202, 0, 32, 255)])
# blue_white_red=ColorPalette((5, 113, 176), neutral_grey, (202, 0, 32))
white_red = ColorPalette(neutral_grey, (202, 0, 32))