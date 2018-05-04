OUTPATH='/home/axel/fltlog_output'

CAMPAIGNS={
'FENNEC2011':[('b599', '20110614'),
              ('b600', '20120617'),
              ('b601', '20120617'),
              ('b602', '20120618'),
              ('b603', '20120618'),
              ('b604', '20120620'),
              ('b605', '20120621'),
              ('b606', '20120621'),
              ('b607', '20120622'),
              ('b608', '20120622'),
              ('b609', '20120624'),
              ('b610', '20120625'),
              ('b611', '20120625'),
              ('b612', '20120626'),
              ('b613', '20120626'),
              ('b614', '20120627'),
              ('b615', '20120628')],
'FENNEC2012': [('b698', '20120601'),
               ('b699', '20120606'),
               ('b700', '20120608'),              
               ('b701', '20120609'),
               ('b702', '20120610'), 
               ('b703', '20120610'),
               ('b704', '20120611'),
               ('b705', '20120612'),
               ('b706', '20120614'),
               ('b707', '20120615'),
               ('b708', '20120616'),
               ('b709', '20120617'),
               ('b710', '20120618'),
               ('b711', '20120619')],
'GAUGE2014': [('b848', '20140515'),
		     ('b849', '20140516'),
		     ('b850', '20140521'),
		     ('b851', '20140617'),
		     ('b852', '20140618'),
		     ('b853', '20140630'),
		     ('b854', '20140630'),
		     ('b855', '20140701'),
		     ('b856', '20140701'),
		     ('b857', '20140702'),
		     ('b858', '20140702'),
		     ('b859', '20140703'),
		     ('b860', '20140704'),
		     ('b862', '20140715'),
		     ('b863', '20140723'),
		     ('b864', '20140901'),
		     ('b865', '20140901'),
		     ('b866', '20140902'),
		     ('b867', '20140902'),
		     ('b868', '20140904'),
		     ('b871', '20140911')],
'PIKNMIX2014': [('b873', '20141120'),
		       ('b874', '20141121'),
   		  ('b875', '20141128'),
		  ('b876', '20141130'),
		  ('b877', '20141201'),
		  ('b878', '20141202'),
		  ('b879', '20141203'),
		  ('b880', '20141205'),
		  ('b881', '20141206'),
		  ('b882', '20141209'),
		  ('b883', '20141213'),
		  ('b884', '20141214')],
'COSMICS': [('b887', '20150217'),
	    ('b888', '20150220'),
	    ('b889', '20150305'),
            ('b890', '20150306'),
            ('b891', '20150308'),
            ('b892', '20150309'),
            ('b893', '20150310'),
            ('b894', '20150311'),
            ('b895', '20150313'),
            ('b896', '20150317'),
            ('b897', '20150318'),
            ('b898', '20150319'),
            ('b899', '20150321'),
            ('b900', '20150322'),
            ('b901', '20150323')],
'SPRING2015': [('b903', '20150430'),
               ('b904', '20150507'),
               ('b905', '20150512'),
               ('b906', '20150512'),
               ('b907', '20150513'),
               ('b908', '20150520'),
               ('b909', '20150521'),
               ('b910', '20150526'),
               ('b911', '20150528'),
               ('b912', '20150609'),
               ('b913', '20150623')],
'ICEDTEST2015': [('b914', '20150713'),
                 ('b915', '20150715'),
                 ('b916', '20150521'),
                 ('b917', '20150522'),
                 ('b918', '20150523')],
'ICED2015': [('b919', '20150806'),
             ('b920', '20150807'),
             ('b921', '20150810'),
             ('b922', '20150811'),
             ('b923', '20150812'),
             ('b924', '20150812'),
             ('b925', '20150813'),
             ('b926', '20150814'),
             ('b927', '20150815'),
             ('b928', '20150816'),
             ('b929', '20150817'),
             ('b930', '20150818'),
             ('b931', '20150819'),
             ('b932', '20150820'),
             ('b933', '20150821'),
             ('b934', '20150825')],
'WINTEX2016': [('b935', '20160115'),
               ('b936', '20160119'),
               ('b937', '20160122'),
               ('b938', '20160208'),
               ('b939', '20160209'),
               ('b940', '20160210'),
               ('b941', '20160211'),
               ('b942', '20160215'),
               ('b943', '20160215'),
               ('b944', '20160216'),
               ('b945', '20160218'),
               ('b946', '20160219'),
               ('b947', '20160303'),
               ('b948', '20160304'),
               ('b949', '20160309'),
               ('b950', '20160314'),
               ('b951', '20160316'),
               ('b952', '20160817')],
'MONSOON2016': [('b956', '20160611'),
                ('b957', '20160612'),
                ('b958', '20160613'),
                ('b959', '20160621'),
                ('b960', '20160622'),
                ('b961', '20160623'),
                ('b962', '20160624'),
                ('b963', '20160625'),
                ('b964', '20160626'),
                ('b965', '20160626'),
                ('b966', '20160627'),
                ('b967', '20160628'),
                ('b968', '20160630'),
                ('b969', '20160702'),
                ('b970', '20160703'),
                ('b971', '20160704'),
                ('b972', '20160705'),
                ('b973', '20160706'),
                ('b974', '20160707'),
                ('b975', '20160709'),
                ('b976', '20160710'),
                ('b977', '20160711')]}







import file_collector
import sys

if len(sys.argv) <= 1:
    sys.stdout.write('\nNot enough input. Submit campaign name. Campaigns available:\n\n')
    for k in sorted(CAMPAIGNS.keys()):
        sys.stdout.write('%s\n' % (k,))
    sys.stdout.write('\nLeaving ...\n\n')
    sys.exit()


if not sys.argv[1].upper() in CAMPAIGNS.keys():
    sys.stdout.write('\nFlight Campaign information not available. Campaigns available:\n\n')
    for k in sorted(CAMPAIGNS.keys()):
        sys.stdout.write('%s\n' % (k,))
    sys.stdout.write('\nLeaving ...\n\n')
    sys.exit(0)
else:
    sys.stdout.write('\nCollecting files for %s. It will take some time.\n\n' % (sys.argv[1].upper(),))


iput=CAMPAIGNS[sys.argv[1].upper()]


for fid, date_string in iput:
    #flog_list=faampy.fltlog.file_collector.FltLog_file_list(fid, date_string, outpath='/home/axel/fltlog_output')
    flog_list = file_collector.process(fid, date_string, outpath=OUTPATH)
    print(flog_list)

