# -*- coding: utf-8 -*-
"""Unicode to 8-bit charset transliteration codec.

This package contains codecs for transliterating ISO 10646 texts into
best-effort representations using smaller coded character sets (ASCII,
ISO 8859, etc.).  The translation tables used by the codecs are from
the ``transtab`` collection by Markus Kuhn.

:copyright: the translitcodec authors and developers, see AUTHORS.
:license: MIT, see LICENSE for more details.

"""
import codecs
import sys
import unicodedata


def long_encode(input, errors='strict'):
    """Transliterate to 8 bit using as many letters as needed.

    For example, \u00e4 LATIN SMALL LETTER A WITH DIAERESIS ``ä`` will
    be replaced with ``ae``.

    """
    if not isinstance(input, unicode):
        input = unicode(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(long_table), length

def short_encode(input, errors='strict'):
    """Transliterate to 8 bit using as few letters as possible.

    For example, \u00e4 LATIN SMALL LETTER A WITH DIAERESIS ``ä`` will
    be replaced with ``a``.

    """
    if not isinstance(input, unicode):
        input = unicode(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(short_table), length

def single_encode(input, errors='strict'):
    """Transliterate to 8 bit using only single letter replacements.

    For example, \u2639 WHITE FROWNING FACE ``☹`` will be passed
    through unchanged.

    """
    if not isinstance(input, unicode):
        input = unicode(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(single_table), length

def no_decode(input, errors='strict'):
    raise TypeError("transliterating codec does not support decode.")

def _double_encoding_factory(encoder, byte_encoder, byte_encoding):
    """Send the transliterated output to another codec."""
    def dbl_encode(input, errors='strict'):
        uni, length = encoder(input, errors)
        return byte_encoder(uni, errors)[0], length
    dbl_encode.__name__ = '%s_%s' % (encoder.__name__, byte_encoding)
    return dbl_encode

def trans_search(encoding):
    """Lookup transliterating codecs."""
    if encoding == 'transliterate':
        return codecs.CodecInfo(long_encode, no_decode)

    # translit/long/utf8
    # translit/one
    # translit/short/ascii

    if encoding.startswith('translit/'):
        parts = encoding.split('/')
        if parts[1] == 'long':
            encoder = long_encode
        elif parts[1] == 'short':
            encoder = short_encode
        elif parts[1] == 'one':
            encoder = single_encode
        else:
            return None

        if len(parts) == 2:
            pass
        elif len(parts) == 3:
            byte_enc = parts[2]
            byte_encoder = codecs.lookup(byte_enc).encode
            encoder = _double_encoding_factory(encoder, byte_encoder, byte_enc)
        else:
            return None
        return codecs.CodecInfo(encoder, no_decode)
    return None

codecs.register(trans_search)

### Code below is generated by update_table.py; do not edit.
### >

long_table = {
  160: u' ',
  161: u'!',
  162: u'c',
  163: u'GBP',
  165: u'Y',
  166: u'|',
  167: u'S',
  168: u'"',
  169: u'(c)',
  170: u'a',
  171: u'<<',
  172: u'-',
  173: u'-',
  174: u'(R)',
  175: u'-',
  176: u' ',
  177: u'+/-',
  178: u'^2',
  179: u'^3',
  180: u"'",
  181: u'\u03bc',
  182: u'P',
  183: u'.',
  184: u',',
  185: u'^1',
  186: u'o',
  187: u'>>',
  188: u' 1/4',
  189: u' 1/2',
  190: u' 3/4',
  191: u'?',
  192: u'A',
  193: u'A',
  194: u'A',
  195: u'A',
  196: u'Ae',
  197: u'Aa',
  198: u'AE',
  199: u'C',
  200: u'E',
  201: u'E',
  202: u'E',
  203: u'E',
  204: u'I',
  205: u'I',
  206: u'I',
  207: u'I',
  208: u'D',
  209: u'N',
  210: u'O',
  211: u'O',
  212: u'O',
  213: u'O',
  214: u'Oe',
  215: u'x',
  216: u'O',
  217: u'U',
  218: u'U',
  219: u'U',
  220: u'Ue',
  221: u'Y',
  222: u'Th',
  223: u'ss',
  224: u'a',
  225: u'a',
  226: u'a',
  227: u'a',
  228: u'ae',
  229: u'aa',
  230: u'ae',
  231: u'c',
  232: u'e',
  233: u'e',
  234: u'e',
  235: u'e',
  236: u'i',
  237: u'i',
  238: u'i',
  239: u'i',
  240: u'd',
  241: u'n',
  242: u'o',
  243: u'o',
  244: u'o',
  245: u'o',
  246: u'oe',
  247: u':',
  248: u'o',
  249: u'u',
  250: u'u',
  251: u'u',
  252: u'ue',
  253: u'y',
  254: u'th',
  255: u'y',
  256: u'A',
  257: u'a',
  258: u'A',
  259: u'a',
  260: u'A',
  261: u'a',
  262: u'C',
  263: u'c',
  264: u'Ch',
  265: u'ch',
  266: u'C',
  267: u'c',
  268: u'C',
  269: u'c',
  270: u'D',
  271: u'd',
  272: u'D',
  273: u'd',
  274: u'E',
  275: u'e',
  276: u'E',
  277: u'e',
  278: u'E',
  279: u'e',
  280: u'E',
  281: u'e',
  282: u'E',
  283: u'e',
  284: u'Gh',
  285: u'gh',
  286: u'G',
  287: u'g',
  288: u'G',
  289: u'g',
  290: u'G',
  291: u'g',
  292: u'Hh',
  293: u'hh',
  294: u'H',
  295: u'h',
  296: u'I',
  297: u'i',
  298: u'I',
  299: u'i',
  300: u'I',
  301: u'i',
  302: u'I',
  303: u'i',
  304: u'I',
  305: u'i',
  306: u'IJ',
  307: u'ij',
  308: u'Jh',
  309: u'jh',
  310: u'K',
  311: u'k',
  312: u'k',
  313: u'L',
  314: u'l',
  315: u'L',
  316: u'l',
  317: u'L',
  318: u'l',
  319: u'L\xb7',
  320: u'l\xb7',
  321: u'L',
  322: u'l',
  323: u'N',
  324: u'n',
  325: u'N',
  326: u'n',
  327: u'N',
  328: u'n',
  329: u"'n",
  330: u'NG',
  331: u'ng',
  332: u'O',
  333: u'o',
  334: u'O',
  335: u'o',
  336: u'O',
  337: u'o',
  338: u'OE',
  339: u'oe',
  340: u'R',
  341: u'r',
  342: u'R',
  343: u'r',
  344: u'R',
  345: u'r',
  346: u'S',
  347: u's',
  348: u'Sh',
  349: u'sh',
  350: u'S',
  351: u's',
  352: u'S',
  353: u's',
  354: u'T',
  355: u't',
  356: u'T',
  357: u't',
  358: u'T',
  359: u't',
  360: u'U',
  361: u'u',
  362: u'U',
  363: u'u',
  364: u'U',
  365: u'u',
  366: u'U',
  367: u'u',
  368: u'U',
  369: u'u',
  370: u'U',
  371: u'u',
  372: u'W',
  373: u'w',
  374: u'Y',
  375: u'y',
  376: u'Y',
  377: u'Z',
  378: u'z',
  379: u'Z',
  380: u'z',
  381: u'Z',
  382: u'z',
  383: u's',
  402: u'f',
  536: u'\u015e',
  537: u'\u015f',
  538: u'\u0162',
  539: u'\u0163',
  697: u'\u2032',
  699: u'\u2018',
  700: u'\u2019',
  701: u'\u201b',
  710: u'^',
  712: u"'",
  713: u'\xaf',
  716: u',',
  720: u':',
  730: u'\xb0',
  732: u'~',
  733: u'"',
  884: u"'",
  885: u',',
  894: u';',
  7682: u'B',
  7683: u'b',
  7690: u'D',
  7691: u'd',
  7710: u'F',
  7711: u'f',
  7744: u'M',
  7745: u'm',
  7766: u'P',
  7767: u'p',
  7776: u'S',
  7777: u's',
  7786: u'T',
  7787: u't',
  7808: u'W',
  7809: u'w',
  7810: u'W',
  7811: u'w',
  7812: u'W',
  7813: u'w',
  7922: u'Y',
  7923: u'y',
  8192: u' ',
  8193: u'  ',
  8194: u' ',
  8195: u'  ',
  8196: u' ',
  8197: u' ',
  8198: u' ',
  8199: u' ',
  8200: u' ',
  8201: u' ',
  8202: u'',
  8203: u'',
  8204: u'',
  8205: u'',
  8206: u'',
  8207: u'',
  8208: u'-',
  8209: u'-',
  8210: u'-',
  8211: u'-',
  8212: u'--',
  8213: u'--',
  8214: u'||',
  8215: u'_',
  8216: u"'",
  8217: u"'",
  8218: u"'",
  8219: u"'",
  8220: u'"',
  8221: u'"',
  8222: u'"',
  8223: u'"',
  8224: u'+',
  8225: u'++',
  8226: u'o',
  8227: u'>',
  8228: u'.',
  8229: u'..',
  8230: u'...',
  8231: u'-',
  8234: u'',
  8235: u'',
  8236: u'',
  8237: u'',
  8238: u'',
  8239: u' ',
  8240: u' 0/00',
  8242: u"'",
  8243: u'"',
  8244: u"'''",
  8245: u'`',
  8246: u'``',
  8247: u'```',
  8249: u'<',
  8250: u'>',
  8252: u'!!',
  8254: u'-',
  8259: u'-',
  8260: u'/',
  8264: u'?!',
  8265: u'!?',
  8266: u'7',
  8304: u'^0',
  8308: u'^4',
  8309: u'^5',
  8310: u'^6',
  8311: u'^7',
  8312: u'^8',
  8313: u'^9',
  8314: u'^+',
  8315: u'^-',
  8316: u'^=',
  8317: u'^(',
  8318: u'^)',
  8319: u'^n',
  8320: u'_0',
  8321: u'_1',
  8322: u'_2',
  8323: u'_3',
  8324: u'_4',
  8325: u'_5',
  8326: u'_6',
  8327: u'_7',
  8328: u'_8',
  8329: u'_9',
  8330: u'_+',
  8331: u'_-',
  8332: u'_=',
  8333: u'_(',
  8334: u'_)',
  8364: u'EUR',
  8448: u'a/c',
  8449: u'a/s',
  8451: u'\xb0C',
  8453: u'c/o',
  8454: u'c/u',
  8457: u'\xb0F',
  8467: u'l',
  8470: u'N\xba',
  8471: u'(P)',
  8480: u'[SM]',
  8481: u'TEL',
  8482: u'[TM]',
  8486: u'\u03a9',
  8490: u'K',
  8491: u'\xc5',
  8494: u'e',
  8531: u' 1/3',
  8532: u' 2/3',
  8533: u' 1/5',
  8534: u' 2/5',
  8535: u' 3/5',
  8536: u' 4/5',
  8537: u' 1/6',
  8538: u' 5/6',
  8539: u' 1/8',
  8540: u' 3/8',
  8541: u' 5/8',
  8542: u' 7/8',
  8543: u' 1/',
  8544: u'I',
  8545: u'II',
  8546: u'III',
  8547: u'IV',
  8548: u'V',
  8549: u'VI',
  8550: u'VII',
  8551: u'VIII',
  8552: u'IX',
  8553: u'X',
  8554: u'XI',
  8555: u'XII',
  8556: u'L',
  8557: u'C',
  8558: u'D',
  8559: u'M',
  8560: u'i',
  8561: u'ii',
  8562: u'iii',
  8563: u'iv',
  8564: u'v',
  8565: u'vi',
  8566: u'vii',
  8567: u'viii',
  8568: u'ix',
  8569: u'x',
  8570: u'xi',
  8571: u'xii',
  8572: u'l',
  8573: u'c',
  8574: u'd',
  8575: u'm',
  8592: u'<-',
  8593: u'^',
  8594: u'->',
  8595: u'v',
  8596: u'<->',
  8656: u'<=',
  8658: u'=>',
  8660: u'<=>',
  8722: u'\u2013',
  8725: u'/',
  8726: u'\\',
  8727: u'*',
  8728: u'o',
  8729: u'\xb7',
  8734: u'inf',
  8739: u'|',
  8741: u'||',
  8758: u':',
  8764: u'~',
  8800: u'/=',
  8801: u'=',
  8804: u'<=',
  8805: u'>=',
  8810: u'<<',
  8811: u'>>',
  8853: u'(+)',
  8854: u'(-)',
  8855: u'(x)',
  8856: u'(/)',
  8866: u'|-',
  8867: u'-|',
  8870: u'|-',
  8871: u'|=',
  8872: u'|=',
  8873: u'||-',
  8901: u'\xb7',
  8902: u'*',
  8917: u'#',
  8920: u'<<<',
  8921: u'>>>',
  8943: u'...',
  9001: u'<',
  9002: u'>',
  9216: u'NUL',
  9217: u'SOH',
  9218: u'STX',
  9219: u'ETX',
  9220: u'EOT',
  9221: u'ENQ',
  9222: u'ACK',
  9223: u'BEL',
  9224: u'BS',
  9225: u'HT',
  9226: u'LF',
  9227: u'VT',
  9228: u'FF',
  9229: u'CR',
  9230: u'SO',
  9231: u'SI',
  9232: u'DLE',
  9233: u'DC1',
  9234: u'DC2',
  9235: u'DC3',
  9236: u'DC4',
  9237: u'NAK',
  9238: u'SYN',
  9239: u'ETB',
  9240: u'CAN',
  9241: u'EM',
  9242: u'SUB',
  9243: u'ESC',
  9244: u'FS',
  9245: u'GS',
  9246: u'RS',
  9247: u'US',
  9248: u'SP',
  9249: u'DEL',
  9251: u'_',
  9252: u'NL',
  9253: u'///',
  9254: u'?',
  9312: u'(1)',
  9313: u'(2)',
  9314: u'(3)',
  9315: u'(4)',
  9316: u'(5)',
  9317: u'(6)',
  9318: u'(7)',
  9319: u'(8)',
  9320: u'(9)',
  9321: u'(10)',
  9322: u'(11)',
  9323: u'(12)',
  9324: u'(13)',
  9325: u'(14)',
  9326: u'(15)',
  9327: u'(16)',
  9328: u'(17)',
  9329: u'(18)',
  9330: u'(19)',
  9331: u'(20)',
  9332: u'(1)',
  9333: u'(2)',
  9334: u'(3)',
  9335: u'(4)',
  9336: u'(5)',
  9337: u'(6)',
  9338: u'(7)',
  9339: u'(8)',
  9340: u'(9)',
  9341: u'(10)',
  9342: u'(11)',
  9343: u'(12)',
  9344: u'(13)',
  9345: u'(14)',
  9346: u'(15)',
  9347: u'(16)',
  9348: u'(17)',
  9349: u'(18)',
  9350: u'(19)',
  9351: u'(20)',
  9352: u'1.',
  9353: u'2.',
  9354: u'3.',
  9355: u'4.',
  9356: u'5.',
  9357: u'6.',
  9358: u'7.',
  9359: u'8.',
  9360: u'9.',
  9361: u'10.',
  9362: u'11.',
  9363: u'12.',
  9364: u'13.',
  9365: u'14.',
  9366: u'15.',
  9367: u'16.',
  9368: u'17.',
  9369: u'18.',
  9370: u'19.',
  9371: u'20.',
  9372: u'(a)',
  9373: u'(b)',
  9374: u'(c)',
  9375: u'(d)',
  9376: u'(e)',
  9377: u'(f)',
  9378: u'(g)',
  9379: u'(h)',
  9380: u'(i)',
  9381: u'(j)',
  9382: u'(k)',
  9383: u'(l)',
  9384: u'(m)',
  9385: u'(n)',
  9386: u'(o)',
  9387: u'(p)',
  9388: u'(q)',
  9389: u'(r)',
  9390: u'(s)',
  9391: u'(t)',
  9392: u'(u)',
  9393: u'(v)',
  9394: u'(w)',
  9395: u'(x)',
  9396: u'(y)',
  9397: u'(z)',
  9398: u'(A)',
  9399: u'(B)',
  9400: u'(C)',
  9401: u'(D)',
  9402: u'(E)',
  9403: u'(F)',
  9404: u'(G)',
  9405: u'(H)',
  9406: u'(I)',
  9407: u'(J)',
  9408: u'(K)',
  9409: u'(L)',
  9410: u'(M)',
  9411: u'(N)',
  9412: u'(O)',
  9413: u'(P)',
  9414: u'(Q)',
  9415: u'(R)',
  9416: u'(S)',
  9417: u'(T)',
  9418: u'(U)',
  9419: u'(V)',
  9420: u'(W)',
  9421: u'(X)',
  9422: u'(Y)',
  9423: u'(Z)',
  9424: u'(a)',
  9425: u'(b)',
  9426: u'(c)',
  9427: u'(d)',
  9428: u'(e)',
  9429: u'(f)',
  9430: u'(g)',
  9431: u'(h)',
  9432: u'(i)',
  9433: u'(j)',
  9434: u'(k)',
  9435: u'(l)',
  9436: u'(m)',
  9437: u'(n)',
  9438: u'(o)',
  9439: u'(p)',
  9440: u'(q)',
  9441: u'(r)',
  9442: u'(s)',
  9443: u'(t)',
  9444: u'(u)',
  9445: u'(v)',
  9446: u'(w)',
  9447: u'(x)',
  9448: u'(y)',
  9449: u'(z)',
  9450: u'(0)',
  9472: u'-',
  9473: u'=',
  9474: u'|',
  9475: u'|',
  9476: u'-',
  9477: u'=',
  9478: u'|',
  9479: u'|',
  9480: u'-',
  9481: u'=',
  9482: u'|',
  9483: u'|',
  9484: u'+',
  9485: u'+',
  9486: u'+',
  9487: u'+',
  9488: u'+',
  9489: u'+',
  9490: u'+',
  9491: u'+',
  9492: u'+',
  9493: u'+',
  9494: u'+',
  9495: u'+',
  9496: u'+',
  9497: u'+',
  9498: u'+',
  9499: u'+',
  9500: u'+',
  9501: u'+',
  9502: u'+',
  9503: u'+',
  9504: u'+',
  9505: u'+',
  9506: u'+',
  9507: u'+',
  9508: u'+',
  9509: u'+',
  9510: u'+',
  9511: u'+',
  9512: u'+',
  9513: u'+',
  9514: u'+',
  9515: u'+',
  9516: u'+',
  9517: u'+',
  9518: u'+',
  9519: u'+',
  9520: u'+',
  9521: u'+',
  9522: u'+',
  9523: u'+',
  9524: u'+',
  9525: u'+',
  9526: u'+',
  9527: u'+',
  9528: u'+',
  9529: u'+',
  9530: u'+',
  9531: u'+',
  9532: u'+',
  9533: u'+',
  9534: u'+',
  9535: u'+',
  9536: u'+',
  9537: u'+',
  9538: u'+',
  9539: u'+',
  9540: u'+',
  9541: u'+',
  9542: u'+',
  9543: u'+',
  9544: u'+',
  9545: u'+',
  9546: u'+',
  9547: u'+',
  9548: u'-',
  9549: u'=',
  9550: u'|',
  9551: u'|',
  9552: u'=',
  9553: u'|',
  9554: u'+',
  9555: u'+',
  9556: u'+',
  9557: u'+',
  9558: u'+',
  9559: u'+',
  9560: u'+',
  9561: u'+',
  9562: u'+',
  9563: u'+',
  9564: u'+',
  9565: u'+',
  9566: u'+',
  9567: u'+',
  9568: u'+',
  9569: u'+',
  9570: u'+',
  9571: u'+',
  9572: u'+',
  9573: u'+',
  9574: u'+',
  9575: u'+',
  9576: u'+',
  9577: u'+',
  9578: u'+',
  9579: u'+',
  9580: u'+',
  9581: u'+',
  9582: u'+',
  9583: u'+',
  9584: u'+',
  9585: u'/',
  9586: u'\\',
  9587: u'X',
  9596: u'-',
  9597: u'|',
  9598: u'-',
  9599: u'|',
  9675: u'o',
  9702: u'o',
  9733: u'*',
  9734: u'*',
  9746: u'X',
  9747: u'X',
  9785: u':-(',
  9786: u':-)',
  9787: u'(-:',
  9837: u'b',
  9839: u'#',
  9985: u'%<',
  9986: u'%<',
  9987: u'%<',
  9988: u'%<',
  9996: u'V',
  10003: u'\u221a',
  10004: u'\u221a',
  10005: u'x',
  10006: u'x',
  10007: u'X',
  10008: u'X',
  10009: u'+',
  10010: u'+',
  10011: u'+',
  10012: u'+',
  10013: u'+',
  10014: u'+',
  10015: u'+',
  10016: u'+',
  10017: u'*',
  10018: u'+',
  10019: u'+',
  10020: u'+',
  10021: u'+',
  10022: u'+',
  10023: u'+',
  10025: u'*',
  10026: u'*',
  10027: u'*',
  10028: u'*',
  10029: u'*',
  10030: u'*',
  10031: u'*',
  10032: u'*',
  10033: u'*',
  10034: u'*',
  10035: u'*',
  10036: u'*',
  10037: u'*',
  10038: u'*',
  10039: u'*',
  10040: u'*',
  10041: u'*',
  10042: u'*',
  10043: u'*',
  10044: u'*',
  10045: u'*',
  10046: u'*',
  10047: u'*',
  10048: u'*',
  10049: u'*',
  10050: u'*',
  10051: u'*',
  10052: u'*',
  10053: u'*',
  10054: u'*',
  10055: u'*',
  10056: u'*',
  10057: u'*',
  10058: u'*',
  10059: u'*',
  64256: u'ff',
  64257: u'fi',
  64258: u'fl',
  64259: u'ffi',
  64260: u'ffl',
  64261: u'\u017ft',
  64262: u'st',
  65279: u'',
  65533: u'?',
}

short_table = {
  160: u' ',
  161: u'!',
  162: u'c',
  163: u'GBP',
  165: u'Y',
  166: u'|',
  167: u'S',
  168: u'"',
  169: u'c',
  170: u'a',
  171: u'<<',
  172: u'-',
  173: u'-',
  174: u'(R)',
  175: u'-',
  176: u' ',
  177: u'+/-',
  178: u'2',
  179: u'3',
  180: u"'",
  181: u'u',
  182: u'P',
  183: u'.',
  184: u',',
  185: u'1',
  186: u'o',
  187: u'>>',
  188: u' 1/4',
  189: u' 1/2',
  190: u' 3/4',
  191: u'?',
  192: u'A',
  193: u'A',
  194: u'A',
  195: u'A',
  196: u'A',
  197: u'A',
  198: u'A',
  199: u'C',
  200: u'E',
  201: u'E',
  202: u'E',
  203: u'E',
  204: u'I',
  205: u'I',
  206: u'I',
  207: u'I',
  208: u'D',
  209: u'N',
  210: u'O',
  211: u'O',
  212: u'O',
  213: u'O',
  214: u'O',
  215: u'x',
  216: u'O',
  217: u'U',
  218: u'U',
  219: u'U',
  220: u'U',
  221: u'Y',
  222: u'Th',
  223: u'\u03b2',
  224: u'a',
  225: u'a',
  226: u'a',
  227: u'a',
  228: u'a',
  229: u'a',
  230: u'a',
  231: u'c',
  232: u'e',
  233: u'e',
  234: u'e',
  235: u'e',
  236: u'i',
  237: u'i',
  238: u'i',
  239: u'i',
  240: u'd',
  241: u'n',
  242: u'o',
  243: u'o',
  244: u'o',
  245: u'o',
  246: u'o',
  247: u':',
  248: u'o',
  249: u'u',
  250: u'u',
  251: u'u',
  252: u'u',
  253: u'y',
  254: u'th',
  255: u'y',
  256: u'A',
  257: u'a',
  258: u'A',
  259: u'a',
  260: u'A',
  261: u'a',
  262: u'C',
  263: u'c',
  264: u'C',
  265: u'c',
  266: u'C',
  267: u'c',
  268: u'C',
  269: u'c',
  270: u'D',
  271: u'd',
  272: u'D',
  273: u'd',
  274: u'E',
  275: u'e',
  276: u'E',
  277: u'e',
  278: u'E',
  279: u'e',
  280: u'E',
  281: u'e',
  282: u'E',
  283: u'e',
  284: u'G',
  285: u'g',
  286: u'G',
  287: u'g',
  288: u'G',
  289: u'g',
  290: u'G',
  291: u'g',
  292: u'H',
  293: u'h',
  294: u'H',
  295: u'h',
  296: u'I',
  297: u'i',
  298: u'I',
  299: u'i',
  300: u'I',
  301: u'i',
  302: u'I',
  303: u'i',
  304: u'I',
  305: u'i',
  306: u'IJ',
  307: u'ij',
  308: u'J',
  309: u'j',
  310: u'K',
  311: u'k',
  312: u'k',
  313: u'L',
  314: u'l',
  315: u'L',
  316: u'l',
  317: u'L',
  318: u'l',
  319: u'L.',
  320: u'l.',
  321: u'L',
  322: u'l',
  323: u'N',
  324: u'n',
  325: u'N',
  326: u'n',
  327: u'N',
  328: u'n',
  329: u"'n",
  330: u'N',
  331: u'n',
  332: u'O',
  333: u'o',
  334: u'O',
  335: u'o',
  336: u'O',
  337: u'o',
  338: u'OE',
  339: u'oe',
  340: u'R',
  341: u'r',
  342: u'R',
  343: u'r',
  344: u'R',
  345: u'r',
  346: u'S',
  347: u's',
  348: u'S',
  349: u's',
  350: u'S',
  351: u's',
  352: u'S',
  353: u's',
  354: u'T',
  355: u't',
  356: u'T',
  357: u't',
  358: u'T',
  359: u't',
  360: u'U',
  361: u'u',
  362: u'U',
  363: u'u',
  364: u'U',
  365: u'u',
  366: u'U',
  367: u'u',
  368: u'U',
  369: u'u',
  370: u'U',
  371: u'u',
  372: u'W',
  373: u'w',
  374: u'Y',
  375: u'y',
  376: u'Y',
  377: u'Z',
  378: u'z',
  379: u'Z',
  380: u'z',
  381: u'Z',
  382: u'z',
  383: u's',
  402: u'f',
  536: u'S',
  537: u's',
  538: u'T',
  539: u't',
  697: u"'",
  699: u'\u2018',
  700: u"'",
  701: u'\u201b',
  710: u'^',
  712: u"'",
  713: u'\xaf',
  716: u',',
  720: u':',
  730: u'\xb0',
  732: u'~',
  733: u'"',
  884: u"'",
  885: u',',
  894: u';',
  7682: u'B',
  7683: u'b',
  7690: u'D',
  7691: u'd',
  7710: u'F',
  7711: u'f',
  7744: u'M',
  7745: u'm',
  7766: u'P',
  7767: u'p',
  7776: u'S',
  7777: u's',
  7786: u'T',
  7787: u't',
  7808: u'W',
  7809: u'w',
  7810: u'W',
  7811: u'w',
  7812: u'W',
  7813: u'w',
  7922: u'Y',
  7923: u'y',
  8192: u' ',
  8193: u'  ',
  8194: u' ',
  8195: u'  ',
  8196: u' ',
  8197: u' ',
  8198: u' ',
  8199: u' ',
  8200: u' ',
  8201: u' ',
  8202: u'',
  8203: u'',
  8204: u'',
  8205: u'',
  8206: u'',
  8207: u'',
  8208: u'-',
  8209: u'-',
  8210: u'-',
  8211: u'-',
  8212: u'--',
  8213: u'--',
  8214: u'||',
  8215: u'_',
  8216: u"'",
  8217: u"'",
  8218: u"'",
  8219: u"'",
  8220: u'"',
  8221: u'"',
  8222: u'"',
  8223: u'"',
  8224: u'+',
  8225: u'++',
  8226: u'o',
  8227: u'>',
  8228: u'.',
  8229: u'..',
  8230: u'...',
  8231: u'-',
  8234: u'',
  8235: u'',
  8236: u'',
  8237: u'',
  8238: u'',
  8239: u' ',
  8240: u' 0/00',
  8242: u"'",
  8243: u'"',
  8244: u"'''",
  8245: u'`',
  8246: u'``',
  8247: u'```',
  8249: u'<',
  8250: u'>',
  8252: u'!!',
  8254: u'-',
  8259: u'-',
  8260: u'/',
  8264: u'?!',
  8265: u'!?',
  8266: u'7',
  8304: u'0',
  8308: u'4',
  8309: u'5',
  8310: u'6',
  8311: u'7',
  8312: u'8',
  8313: u'9',
  8314: u'+',
  8315: u'-',
  8316: u'=',
  8317: u'(',
  8318: u')',
  8319: u'n',
  8320: u'0',
  8321: u'1',
  8322: u'2',
  8323: u'3',
  8324: u'4',
  8325: u'5',
  8326: u'6',
  8327: u'7',
  8328: u'8',
  8329: u'9',
  8330: u'+',
  8331: u'-',
  8332: u'=',
  8333: u'(',
  8334: u')',
  8364: u'E',
  8448: u'a/c',
  8449: u'a/s',
  8451: u'C',
  8453: u'c/o',
  8454: u'c/u',
  8457: u'F',
  8467: u'l',
  8470: u'No',
  8471: u'(P)',
  8480: u'[SM]',
  8481: u'TEL',
  8482: u'[TM]',
  8486: u'ohm',
  8490: u'K',
  8491: u'\xc5',
  8494: u'e',
  8531: u' 1/3',
  8532: u' 2/3',
  8533: u' 1/5',
  8534: u' 2/5',
  8535: u' 3/5',
  8536: u' 4/5',
  8537: u' 1/6',
  8538: u' 5/6',
  8539: u' 1/8',
  8540: u' 3/8',
  8541: u' 5/8',
  8542: u' 7/8',
  8543: u' 1/',
  8544: u'I',
  8545: u'II',
  8546: u'III',
  8547: u'IV',
  8548: u'V',
  8549: u'VI',
  8550: u'VII',
  8551: u'VIII',
  8552: u'IX',
  8553: u'X',
  8554: u'XI',
  8555: u'XII',
  8556: u'L',
  8557: u'C',
  8558: u'D',
  8559: u'M',
  8560: u'i',
  8561: u'ii',
  8562: u'iii',
  8563: u'iv',
  8564: u'v',
  8565: u'vi',
  8566: u'vii',
  8567: u'viii',
  8568: u'ix',
  8569: u'x',
  8570: u'xi',
  8571: u'xii',
  8572: u'l',
  8573: u'c',
  8574: u'd',
  8575: u'm',
  8592: u'<-',
  8593: u'^',
  8594: u'->',
  8595: u'v',
  8596: u'<->',
  8656: u'<=',
  8658: u'=>',
  8660: u'<=>',
  8722: u'-',
  8725: u'/',
  8726: u'\\',
  8727: u'*',
  8728: u'o',
  8729: u'\xb7',
  8734: u'inf',
  8739: u'|',
  8741: u'||',
  8758: u':',
  8764: u'~',
  8800: u'/=',
  8801: u'=',
  8804: u'<=',
  8805: u'>=',
  8810: u'<<',
  8811: u'>>',
  8853: u'(+)',
  8854: u'(-)',
  8855: u'(x)',
  8856: u'(/)',
  8866: u'|-',
  8867: u'-|',
  8870: u'|-',
  8871: u'|=',
  8872: u'|=',
  8873: u'||-',
  8901: u'\xb7',
  8902: u'*',
  8917: u'#',
  8920: u'<<<',
  8921: u'>>>',
  8943: u'...',
  9001: u'<',
  9002: u'>',
  9216: u'NUL',
  9217: u'SOH',
  9218: u'STX',
  9219: u'ETX',
  9220: u'EOT',
  9221: u'ENQ',
  9222: u'ACK',
  9223: u'BEL',
  9224: u'BS',
  9225: u'HT',
  9226: u'LF',
  9227: u'VT',
  9228: u'FF',
  9229: u'CR',
  9230: u'SO',
  9231: u'SI',
  9232: u'DLE',
  9233: u'DC1',
  9234: u'DC2',
  9235: u'DC3',
  9236: u'DC4',
  9237: u'NAK',
  9238: u'SYN',
  9239: u'ETB',
  9240: u'CAN',
  9241: u'EM',
  9242: u'SUB',
  9243: u'ESC',
  9244: u'FS',
  9245: u'GS',
  9246: u'RS',
  9247: u'US',
  9248: u'SP',
  9249: u'DEL',
  9251: u'_',
  9252: u'NL',
  9253: u'///',
  9254: u'?',
  9312: u'1',
  9313: u'2',
  9314: u'3',
  9315: u'4',
  9316: u'5',
  9317: u'6',
  9318: u'7',
  9319: u'8',
  9320: u'9',
  9321: u'(10)',
  9322: u'(11)',
  9323: u'(12)',
  9324: u'(13)',
  9325: u'(14)',
  9326: u'(15)',
  9327: u'(16)',
  9328: u'(17)',
  9329: u'(18)',
  9330: u'(19)',
  9331: u'(20)',
  9332: u'1',
  9333: u'2',
  9334: u'3',
  9335: u'4',
  9336: u'5',
  9337: u'6',
  9338: u'7',
  9339: u'8',
  9340: u'9',
  9341: u'(10)',
  9342: u'(11)',
  9343: u'(12)',
  9344: u'(13)',
  9345: u'(14)',
  9346: u'(15)',
  9347: u'(16)',
  9348: u'(17)',
  9349: u'(18)',
  9350: u'(19)',
  9351: u'(20)',
  9352: u'1',
  9353: u'2',
  9354: u'3',
  9355: u'4',
  9356: u'5',
  9357: u'6',
  9358: u'7',
  9359: u'8',
  9360: u'9',
  9361: u'10.',
  9362: u'11.',
  9363: u'12.',
  9364: u'13.',
  9365: u'14.',
  9366: u'15.',
  9367: u'16.',
  9368: u'17.',
  9369: u'18.',
  9370: u'19.',
  9371: u'20.',
  9372: u'a',
  9373: u'b',
  9374: u'c',
  9375: u'd',
  9376: u'e',
  9377: u'f',
  9378: u'g',
  9379: u'h',
  9380: u'i',
  9381: u'j',
  9382: u'k',
  9383: u'l',
  9384: u'm',
  9385: u'n',
  9386: u'o',
  9387: u'p',
  9388: u'q',
  9389: u'r',
  9390: u's',
  9391: u't',
  9392: u'u',
  9393: u'v',
  9394: u'w',
  9395: u'x',
  9396: u'y',
  9397: u'z',
  9398: u'A',
  9399: u'B',
  9400: u'C',
  9401: u'D',
  9402: u'E',
  9403: u'F',
  9404: u'G',
  9405: u'H',
  9406: u'I',
  9407: u'J',
  9408: u'K',
  9409: u'L',
  9410: u'M',
  9411: u'N',
  9412: u'O',
  9413: u'P',
  9414: u'Q',
  9415: u'R',
  9416: u'S',
  9417: u'T',
  9418: u'U',
  9419: u'V',
  9420: u'W',
  9421: u'X',
  9422: u'Y',
  9423: u'Z',
  9424: u'a',
  9425: u'b',
  9426: u'c',
  9427: u'd',
  9428: u'e',
  9429: u'f',
  9430: u'g',
  9431: u'h',
  9432: u'i',
  9433: u'j',
  9434: u'k',
  9435: u'l',
  9436: u'm',
  9437: u'n',
  9438: u'o',
  9439: u'p',
  9440: u'q',
  9441: u'r',
  9442: u's',
  9443: u't',
  9444: u'u',
  9445: u'v',
  9446: u'w',
  9447: u'x',
  9448: u'y',
  9449: u'z',
  9450: u'0',
  9472: u'-',
  9473: u'=',
  9474: u'|',
  9475: u'|',
  9476: u'-',
  9477: u'=',
  9478: u'|',
  9479: u'|',
  9480: u'-',
  9481: u'=',
  9482: u'|',
  9483: u'|',
  9484: u'+',
  9485: u'+',
  9486: u'+',
  9487: u'+',
  9488: u'+',
  9489: u'+',
  9490: u'+',
  9491: u'+',
  9492: u'+',
  9493: u'+',
  9494: u'+',
  9495: u'+',
  9496: u'+',
  9497: u'+',
  9498: u'+',
  9499: u'+',
  9500: u'+',
  9501: u'+',
  9502: u'+',
  9503: u'+',
  9504: u'+',
  9505: u'+',
  9506: u'+',
  9507: u'+',
  9508: u'+',
  9509: u'+',
  9510: u'+',
  9511: u'+',
  9512: u'+',
  9513: u'+',
  9514: u'+',
  9515: u'+',
  9516: u'+',
  9517: u'+',
  9518: u'+',
  9519: u'+',
  9520: u'+',
  9521: u'+',
  9522: u'+',
  9523: u'+',
  9524: u'+',
  9525: u'+',
  9526: u'+',
  9527: u'+',
  9528: u'+',
  9529: u'+',
  9530: u'+',
  9531: u'+',
  9532: u'+',
  9533: u'+',
  9534: u'+',
  9535: u'+',
  9536: u'+',
  9537: u'+',
  9538: u'+',
  9539: u'+',
  9540: u'+',
  9541: u'+',
  9542: u'+',
  9543: u'+',
  9544: u'+',
  9545: u'+',
  9546: u'+',
  9547: u'+',
  9548: u'-',
  9549: u'=',
  9550: u'|',
  9551: u'|',
  9552: u'=',
  9553: u'|',
  9554: u'+',
  9555: u'+',
  9556: u'+',
  9557: u'+',
  9558: u'+',
  9559: u'+',
  9560: u'+',
  9561: u'+',
  9562: u'+',
  9563: u'+',
  9564: u'+',
  9565: u'+',
  9566: u'+',
  9567: u'+',
  9568: u'+',
  9569: u'+',
  9570: u'+',
  9571: u'+',
  9572: u'+',
  9573: u'+',
  9574: u'+',
  9575: u'+',
  9576: u'+',
  9577: u'+',
  9578: u'+',
  9579: u'+',
  9580: u'+',
  9581: u'+',
  9582: u'+',
  9583: u'+',
  9584: u'+',
  9585: u'/',
  9586: u'\\',
  9587: u'X',
  9596: u'-',
  9597: u'|',
  9598: u'-',
  9599: u'|',
  9675: u'o',
  9702: u'o',
  9733: u'*',
  9734: u'*',
  9746: u'X',
  9747: u'X',
  9785: u':-(',
  9786: u':-)',
  9787: u'(-:',
  9837: u'b',
  9839: u'#',
  9985: u'%<',
  9986: u'%<',
  9987: u'%<',
  9988: u'%<',
  9996: u'V',
  10003: u'\u221a',
  10004: u'\u221a',
  10005: u'x',
  10006: u'x',
  10007: u'X',
  10008: u'X',
  10009: u'+',
  10010: u'+',
  10011: u'+',
  10012: u'+',
  10013: u'+',
  10014: u'+',
  10015: u'+',
  10016: u'+',
  10017: u'*',
  10018: u'+',
  10019: u'+',
  10020: u'+',
  10021: u'+',
  10022: u'+',
  10023: u'+',
  10025: u'*',
  10026: u'*',
  10027: u'*',
  10028: u'*',
  10029: u'*',
  10030: u'*',
  10031: u'*',
  10032: u'*',
  10033: u'*',
  10034: u'*',
  10035: u'*',
  10036: u'*',
  10037: u'*',
  10038: u'*',
  10039: u'*',
  10040: u'*',
  10041: u'*',
  10042: u'*',
  10043: u'*',
  10044: u'*',
  10045: u'*',
  10046: u'*',
  10047: u'*',
  10048: u'*',
  10049: u'*',
  10050: u'*',
  10051: u'*',
  10052: u'*',
  10053: u'*',
  10054: u'*',
  10055: u'*',
  10056: u'*',
  10057: u'*',
  10058: u'*',
  10059: u'*',
  64256: u'ff',
  64257: u'fi',
  64258: u'fl',
  64259: u'ffi',
  64260: u'ffl',
  64261: u'st',
  64262: u'st',
  65279: u'',
  65533: u'?',
}

single_table = {
  160: u' ',
  161: u'!',
  162: u'c',
  165: u'Y',
  166: u'|',
  167: u'S',
  168: u'"',
  169: u'c',
  170: u'a',
  172: u'-',
  173: u'-',
  175: u'-',
  176: u' ',
  178: u'2',
  179: u'3',
  180: u"'",
  181: u'u',
  182: u'P',
  183: u'.',
  184: u',',
  185: u'1',
  186: u'o',
  191: u'?',
  192: u'A',
  193: u'A',
  194: u'A',
  195: u'A',
  196: u'A',
  197: u'A',
  198: u'A',
  199: u'C',
  200: u'E',
  201: u'E',
  202: u'E',
  203: u'E',
  204: u'I',
  205: u'I',
  206: u'I',
  207: u'I',
  208: u'D',
  209: u'N',
  210: u'O',
  211: u'O',
  212: u'O',
  213: u'O',
  214: u'O',
  215: u'x',
  216: u'O',
  217: u'U',
  218: u'U',
  219: u'U',
  220: u'U',
  221: u'Y',
  223: u'\u03b2',
  224: u'a',
  225: u'a',
  226: u'a',
  227: u'a',
  228: u'a',
  229: u'a',
  230: u'a',
  231: u'c',
  232: u'e',
  233: u'e',
  234: u'e',
  235: u'e',
  236: u'i',
  237: u'i',
  238: u'i',
  239: u'i',
  240: u'd',
  241: u'n',
  242: u'o',
  243: u'o',
  244: u'o',
  245: u'o',
  246: u'o',
  247: u':',
  248: u'o',
  249: u'u',
  250: u'u',
  251: u'u',
  252: u'u',
  253: u'y',
  255: u'y',
  256: u'A',
  257: u'a',
  258: u'A',
  259: u'a',
  260: u'A',
  261: u'a',
  262: u'C',
  263: u'c',
  264: u'C',
  265: u'c',
  266: u'C',
  267: u'c',
  268: u'C',
  269: u'c',
  270: u'D',
  271: u'd',
  272: u'D',
  273: u'd',
  274: u'E',
  275: u'e',
  276: u'E',
  277: u'e',
  278: u'E',
  279: u'e',
  280: u'E',
  281: u'e',
  282: u'E',
  283: u'e',
  284: u'G',
  285: u'g',
  286: u'G',
  287: u'g',
  288: u'G',
  289: u'g',
  290: u'G',
  291: u'g',
  292: u'H',
  293: u'h',
  294: u'H',
  295: u'h',
  296: u'I',
  297: u'i',
  298: u'I',
  299: u'i',
  300: u'I',
  301: u'i',
  302: u'I',
  303: u'i',
  304: u'I',
  305: u'i',
  308: u'J',
  309: u'j',
  310: u'K',
  311: u'k',
  312: u'k',
  313: u'L',
  314: u'l',
  315: u'L',
  316: u'l',
  317: u'L',
  318: u'l',
  321: u'L',
  322: u'l',
  323: u'N',
  324: u'n',
  325: u'N',
  326: u'n',
  327: u'N',
  328: u'n',
  330: u'N',
  331: u'n',
  332: u'O',
  333: u'o',
  334: u'O',
  335: u'o',
  336: u'O',
  337: u'o',
  340: u'R',
  341: u'r',
  342: u'R',
  343: u'r',
  344: u'R',
  345: u'r',
  346: u'S',
  347: u's',
  348: u'S',
  349: u's',
  350: u'S',
  351: u's',
  352: u'S',
  353: u's',
  354: u'T',
  355: u't',
  356: u'T',
  357: u't',
  358: u'T',
  359: u't',
  360: u'U',
  361: u'u',
  362: u'U',
  363: u'u',
  364: u'U',
  365: u'u',
  366: u'U',
  367: u'u',
  368: u'U',
  369: u'u',
  370: u'U',
  371: u'u',
  372: u'W',
  373: u'w',
  374: u'Y',
  375: u'y',
  376: u'Y',
  377: u'Z',
  378: u'z',
  379: u'Z',
  380: u'z',
  381: u'Z',
  382: u'z',
  383: u's',
  402: u'f',
  536: u'S',
  537: u's',
  538: u'T',
  539: u't',
  697: u"'",
  699: u'\u2018',
  700: u"'",
  701: u'\u201b',
  710: u'^',
  712: u"'",
  713: u'\xaf',
  716: u',',
  720: u':',
  730: u'\xb0',
  732: u'~',
  733: u'"',
  884: u"'",
  885: u',',
  894: u';',
  7682: u'B',
  7683: u'b',
  7690: u'D',
  7691: u'd',
  7710: u'F',
  7711: u'f',
  7744: u'M',
  7745: u'm',
  7766: u'P',
  7767: u'p',
  7776: u'S',
  7777: u's',
  7786: u'T',
  7787: u't',
  7808: u'W',
  7809: u'w',
  7810: u'W',
  7811: u'w',
  7812: u'W',
  7813: u'w',
  7922: u'Y',
  7923: u'y',
  8192: u' ',
  8194: u' ',
  8196: u' ',
  8197: u' ',
  8198: u' ',
  8199: u' ',
  8200: u' ',
  8201: u' ',
  8208: u'-',
  8209: u'-',
  8210: u'-',
  8211: u'-',
  8215: u'_',
  8216: u"'",
  8217: u"'",
  8218: u"'",
  8219: u"'",
  8220: u'"',
  8221: u'"',
  8222: u'"',
  8223: u'"',
  8224: u'+',
  8226: u'o',
  8227: u'>',
  8228: u'.',
  8231: u'-',
  8239: u' ',
  8242: u"'",
  8243: u'"',
  8245: u'`',
  8249: u'<',
  8250: u'>',
  8254: u'-',
  8259: u'-',
  8260: u'/',
  8266: u'7',
  8304: u'0',
  8308: u'4',
  8309: u'5',
  8310: u'6',
  8311: u'7',
  8312: u'8',
  8313: u'9',
  8314: u'+',
  8315: u'-',
  8316: u'=',
  8317: u'(',
  8318: u')',
  8319: u'n',
  8320: u'0',
  8321: u'1',
  8322: u'2',
  8323: u'3',
  8324: u'4',
  8325: u'5',
  8326: u'6',
  8327: u'7',
  8328: u'8',
  8329: u'9',
  8330: u'+',
  8331: u'-',
  8332: u'=',
  8333: u'(',
  8334: u')',
  8364: u'E',
  8451: u'C',
  8457: u'F',
  8467: u'l',
  8490: u'K',
  8491: u'\xc5',
  8494: u'e',
  8544: u'I',
  8548: u'V',
  8553: u'X',
  8556: u'L',
  8557: u'C',
  8558: u'D',
  8559: u'M',
  8560: u'i',
  8564: u'v',
  8569: u'x',
  8572: u'l',
  8573: u'c',
  8574: u'd',
  8575: u'm',
  8593: u'^',
  8595: u'v',
  8722: u'-',
  8725: u'/',
  8726: u'\\',
  8727: u'*',
  8728: u'o',
  8729: u'\xb7',
  8739: u'|',
  8758: u':',
  8764: u'~',
  8801: u'=',
  8901: u'\xb7',
  8902: u'*',
  8917: u'#',
  9001: u'<',
  9002: u'>',
  9251: u'_',
  9254: u'?',
  9312: u'1',
  9313: u'2',
  9314: u'3',
  9315: u'4',
  9316: u'5',
  9317: u'6',
  9318: u'7',
  9319: u'8',
  9320: u'9',
  9332: u'1',
  9333: u'2',
  9334: u'3',
  9335: u'4',
  9336: u'5',
  9337: u'6',
  9338: u'7',
  9339: u'8',
  9340: u'9',
  9352: u'1',
  9353: u'2',
  9354: u'3',
  9355: u'4',
  9356: u'5',
  9357: u'6',
  9358: u'7',
  9359: u'8',
  9360: u'9',
  9372: u'a',
  9373: u'b',
  9374: u'c',
  9375: u'd',
  9376: u'e',
  9377: u'f',
  9378: u'g',
  9379: u'h',
  9380: u'i',
  9381: u'j',
  9382: u'k',
  9383: u'l',
  9384: u'm',
  9385: u'n',
  9386: u'o',
  9387: u'p',
  9388: u'q',
  9389: u'r',
  9390: u's',
  9391: u't',
  9392: u'u',
  9393: u'v',
  9394: u'w',
  9395: u'x',
  9396: u'y',
  9397: u'z',
  9398: u'A',
  9399: u'B',
  9400: u'C',
  9401: u'D',
  9402: u'E',
  9403: u'F',
  9404: u'G',
  9405: u'H',
  9406: u'I',
  9407: u'J',
  9408: u'K',
  9409: u'L',
  9410: u'M',
  9411: u'N',
  9412: u'O',
  9413: u'P',
  9414: u'Q',
  9415: u'R',
  9416: u'S',
  9417: u'T',
  9418: u'U',
  9419: u'V',
  9420: u'W',
  9421: u'X',
  9422: u'Y',
  9423: u'Z',
  9424: u'a',
  9425: u'b',
  9426: u'c',
  9427: u'd',
  9428: u'e',
  9429: u'f',
  9430: u'g',
  9431: u'h',
  9432: u'i',
  9433: u'j',
  9434: u'k',
  9435: u'l',
  9436: u'm',
  9437: u'n',
  9438: u'o',
  9439: u'p',
  9440: u'q',
  9441: u'r',
  9442: u's',
  9443: u't',
  9444: u'u',
  9445: u'v',
  9446: u'w',
  9447: u'x',
  9448: u'y',
  9449: u'z',
  9450: u'0',
  9472: u'-',
  9473: u'=',
  9474: u'|',
  9475: u'|',
  9476: u'-',
  9477: u'=',
  9478: u'|',
  9479: u'|',
  9480: u'-',
  9481: u'=',
  9482: u'|',
  9483: u'|',
  9484: u'+',
  9485: u'+',
  9486: u'+',
  9487: u'+',
  9488: u'+',
  9489: u'+',
  9490: u'+',
  9491: u'+',
  9492: u'+',
  9493: u'+',
  9494: u'+',
  9495: u'+',
  9496: u'+',
  9497: u'+',
  9498: u'+',
  9499: u'+',
  9500: u'+',
  9501: u'+',
  9502: u'+',
  9503: u'+',
  9504: u'+',
  9505: u'+',
  9506: u'+',
  9507: u'+',
  9508: u'+',
  9509: u'+',
  9510: u'+',
  9511: u'+',
  9512: u'+',
  9513: u'+',
  9514: u'+',
  9515: u'+',
  9516: u'+',
  9517: u'+',
  9518: u'+',
  9519: u'+',
  9520: u'+',
  9521: u'+',
  9522: u'+',
  9523: u'+',
  9524: u'+',
  9525: u'+',
  9526: u'+',
  9527: u'+',
  9528: u'+',
  9529: u'+',
  9530: u'+',
  9531: u'+',
  9532: u'+',
  9533: u'+',
  9534: u'+',
  9535: u'+',
  9536: u'+',
  9537: u'+',
  9538: u'+',
  9539: u'+',
  9540: u'+',
  9541: u'+',
  9542: u'+',
  9543: u'+',
  9544: u'+',
  9545: u'+',
  9546: u'+',
  9547: u'+',
  9548: u'-',
  9549: u'=',
  9550: u'|',
  9551: u'|',
  9552: u'=',
  9553: u'|',
  9554: u'+',
  9555: u'+',
  9556: u'+',
  9557: u'+',
  9558: u'+',
  9559: u'+',
  9560: u'+',
  9561: u'+',
  9562: u'+',
  9563: u'+',
  9564: u'+',
  9565: u'+',
  9566: u'+',
  9567: u'+',
  9568: u'+',
  9569: u'+',
  9570: u'+',
  9571: u'+',
  9572: u'+',
  9573: u'+',
  9574: u'+',
  9575: u'+',
  9576: u'+',
  9577: u'+',
  9578: u'+',
  9579: u'+',
  9580: u'+',
  9581: u'+',
  9582: u'+',
  9583: u'+',
  9584: u'+',
  9585: u'/',
  9586: u'\\',
  9587: u'X',
  9596: u'-',
  9597: u'|',
  9598: u'-',
  9599: u'|',
  9675: u'o',
  9702: u'o',
  9733: u'*',
  9734: u'*',
  9746: u'X',
  9747: u'X',
  9837: u'b',
  9839: u'#',
  9996: u'V',
  10003: u'\u221a',
  10004: u'\u221a',
  10005: u'x',
  10006: u'x',
  10007: u'X',
  10008: u'X',
  10009: u'+',
  10010: u'+',
  10011: u'+',
  10012: u'+',
  10013: u'+',
  10014: u'+',
  10015: u'+',
  10016: u'+',
  10017: u'*',
  10018: u'+',
  10019: u'+',
  10020: u'+',
  10021: u'+',
  10022: u'+',
  10023: u'+',
  10025: u'*',
  10026: u'*',
  10027: u'*',
  10028: u'*',
  10029: u'*',
  10030: u'*',
  10031: u'*',
  10032: u'*',
  10033: u'*',
  10034: u'*',
  10035: u'*',
  10036: u'*',
  10037: u'*',
  10038: u'*',
  10039: u'*',
  10040: u'*',
  10041: u'*',
  10042: u'*',
  10043: u'*',
  10044: u'*',
  10045: u'*',
  10046: u'*',
  10047: u'*',
  10048: u'*',
  10049: u'*',
  10050: u'*',
  10051: u'*',
  10052: u'*',
  10053: u'*',
  10054: u'*',
  10055: u'*',
  10056: u'*',
  10057: u'*',
  10058: u'*',
  10059: u'*',
  65533: u'?',
}


### <

