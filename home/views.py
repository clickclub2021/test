from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import QuesModel,Name
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import *

# superuser
# username - admin
# password - admin


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
  
        if form.is_valid():
            user = form.save(commit=False)
            #17/7/21 3:00 AM
            mylist = ['mandeepsingh._04','rsmi_sahu__', 'sai_kiran_2398', 'k_o_m_a_l_l_l', 'rajasinha07', '2645swarnima', 'gujju_gujrati_1234', '_its_me_sathwika.__', '__picturesforyou_', 'sathish__nayak', 'ka.rishma_0908_', 'nagendernathpathak', 'ubanitrr', 'saket_tupkari', 'ishitbeladiya007', 'chandraashish', 'vamsi.singampalli.7', 'saisanjeevareddy', 'shubham.gupta_24', '_checkmate8_', 'boudh_prakash', '_praveen_sahu', 'deenanshu', 'js_027', 'shreealways', 'shotbysai_k', 'omni_28_', 'harry_2898', 'shutterbugiiitnr', 'neogy_dipa', 'vasuveersingh', 'manvendra1167', '1399nupur', 'itz_rajkumund_official', 'dnakarani', 'digeshwar_dewangan', '_shruti_131', 'foodiesardarjiii', 'vikas._.ghritlahre', 'kunal_doune', 'rohit__mina', 'kamakshya_negotrip', 'd.i.s.h.a_22', '_hawks', 'nami41171', 'saurabhprasad_19', 'jg_photographyyyyy', 'ankush_19_96', 'kre1th', 'jankilal_dhakad650', 'kavyabondada', 'abinth744', 'ayush_pattnaik_', 'om.agrawal.1048', 'gkgabel', 'rahulmanhar01', 'shutter1200d', 'kutch_the_heart_of_gujarat', 'ks_photography1170', 'vikasprerana', 'abhaypratap5786', 'kushaljain.202', 'vishist_pandey', 'shantanu361', 'thats_vamsi', 'shekhar_patel.142507', 'avijeetsm', 'priyanshi.sharma', 'kshitijm10', 'palashsagarkar', 'vishal_thakur501', 'elgnismai', 'the_.creator_', 'anshshivhare_', 'kumaranil750', 'bit_memes_club', 'shri.dubey', 'mohankumar2677', 'gunisityy', 'gowthamreddy_uppunuri404', 'aravindgopal_sv', 'chaitanyapulavarthi', 'shukla9386', 'the__mature_kid', '0110_prashant', 'rayudu_rahul', 'atish8391', 'khushboo_sori', '_fauji_244', 'saranyakadiyala', 'sanskarsharma_', 'a_uncanny_tale', '_praneethak_', 'tanshis.atelier', 'waseem_chisty', 'parveshbansal47535', 'sri_sai_suhas', 'mihika_kothari', 'avermaz_graphy', 'pixellence.in', 'sacheenpairaikar', 'prateeksaxena25', 'bajajapeksha', 'clickoholic_17', 'astronomical.photography', 'kks.cr2', 'roar_evil_ashish', 'samratbhardwaj97', 'rohitsamanta22', 'blacktiecreation', 'prtkpanda', '_.rashika._11', '_rksratnesh', '__.jaykumar.__', 'rakshapandram_750', 'nutsvedant', 'i.am.hrt', '_sum___it_', 'sashidharkadambari', 'the____supreme', 'cleanv._', 'himanshu_kerosene', 'ksmate03', 'adityaboss9902', 'chandra.kumar.patel07', 'abhilashnayak_626', 'sriuma_mothukuri', 'sanjeethdkundan', 'eclectic_ritvij', 'nxgrawal_3012', 'studiomanaswini', 'anuragsingh92', 'cyn.ss', 'abhinavmi5hra', 'siddharth_dhang', 'shashanksahu_30', 'aayushi.vatsal', 'ashish_vma', 'krish_rlive', '_.rashi18._', 'pr.achi850', 'bhavuparmar009', 'sanjesh_meshram', 'abdussamadvhora', 'nachi__13', 'pandey_adarsh_2798', 'rony_pani', 'vasudev0210', 'tanayspicturesque', 'rishabh08.rj', '_.judu_', 'k_u_m_a_r_21', 'kirtinanjiani', 'i_aman_soni', 'shloktamrakar', 'prianca018', 'naik_d._.gg_', 'jarvis_26_', 'alireza.hadadi.1387', 'suyashsingh_11', 'ayush_swarnkar_', 'sabka.maalik.1', 'nikhilkushwaha14', 'alamarish', 'sai_manaswini_reddy', 'zora_east_gallery', 'upkarpathak', '_09kiki', 'they_call_me.utkarsh', 'skmeshram', 'atulsingh1458', 'siddharthshah3030', 'tambolivanshika', 'munorastogi', 'varshuu_11', 'king_north_mr.roy', 'chandu_gullu8071', 'imsourabh.srb', 'ja.3.rao', 'harsh_khawas', 'best_harshit', 'akashgayakwad123', 'manjulata_diwakar', 'yoursbharat', 'aamantran_aesthetics', 'swapnil_agarwal11', 'shubh_228', 'uwais_uwz', '_its.dhangav.i_', 'deepak_rawte', 'nitinagrawal1001', 'kdblog_official', 'saksham.sav', 'sarthak1702', 'atreya_1997', 'purvijain._', 'nivesh_shukla99', 'vedant_dewangan', 'annu.kriti', 'not.wildstone.guy', '08srijan', 'ammusrivastav', 'raat_ka_reporter', 'angesanand_imw', 'modelhuntz', 'boddu.saikiran17', 'hemanth_challengers', 'adity_0523', 'parimaljichkar', 'sai_teja_15_05', 'nitish.agrawal07', 'photographic_at', 'gautham_5300', 'sanchitmahto', 'pritiagrawal95', 'geo_illusionist', 'rajbhasha_nit_raipur', 'kritikasingh_2408', '_mukulkaushik', 'kajal_verma_12', 'photography_ki_duniyaa', 'pritesh_anjikar', 'modaling_photography__', 'sakshat550', '_jassu_saini_', 'pradumn2999', 'chetan_iocl', 'rahulky', 'iamashutterbug_', 'shalini.ahuja.3576', 'anukrutidas', 'pranay.chinta96', 'shoukat09_', 'artistio_sketchworks', 'naveen_9015', 'azharqspeaks', '_dharm._.sharma_', 'monik_ghanchi', 'vaibhavsawant_8', 'sacroelements', 'yashita_jaggi', 'sourabh123555', 'vikash_kr13', 'paaritosh_sujit', 'vankit3611', 'subhankar.dash', 'duniya_vijay_721', '_or_knob', 'aditya_bhoi', 'varun_panchal.__', 'chandrakarpragati', 'ravi_varma_ankam', 'myself_nandu.palla', 'rajeev_kanwar__', 'bhavesh_o23', 'kbaghel.234', 'theankletgirl', 'pushpakardurgesh', 'anubhaw_dheeren', 'fourth_perspective_', 'bhavin_raichura', '01gunjan666', 'ananthulavijaysai', 'tnakardnahc', 'dev.k.tirkey', 'wholesalewale123', 'veethika._', 'sk_panjwani', 'ahuja_sanjeevani', '_poojapatel0408_', 'shivangi_komre', 'petrichor_snaps', 'bhupesh_verma_', 'khushi.__joshi', 'garginayak', 'devvratsharma28', 'escafade', 'sachin_kalakota', 'tarun.kaushik', 'dandeashritgmail.com2000', 'sadhvika_kadiyala', 'o_sana_o', 'vibrant_vision_photoworks', 'sahyognitrr', 'thegavelmahendra', 'amrutha_koripalli', 'sashreek_singh', 'ravi_rv_09', 'saga_90009', '_yuvraj_kosle_23', 'harshthakur', '_yashasvi08', 'yoursyogesh01', 's_h_u_b_h_a_m_004', 'its_a.b.h.i_j.e.e.t_', 'smritipaikra', 'pratikgahel', 'mukul7283', 'pritam.ready.3', 'hitman_shubham', 'ronsai_boro', 'shreryyy_yy', 'i_m_chetansemwal', 'automaton_1', 'rishavgn', 'angrakha_', 'dineshjani777', 'platinumphotoss', 'extinct_boy_', 'gunikthegeek', '_pixie.realm_', 'priyanshu_douriya', 'jagriti.soni', 'yearbookstartup', 'sandy_3ss', 'sujeetbarsale', 'paritosh_swarnkar', '_p.agarwal_', 'nsharmaz_photography', 'techieanky', 'krishnakant_dehariya', 'shashi_bhushan__', 'amitsinghrajput1995', 'divakar.143', 'n4_narendra', '_priyanka.24', 'raviksn2', 'rajatmurdia', 'kpverma_2001', 'follow.aur_suno_', 'its_gopu.here', 'adityaraj_chowhan', 'shxbhangi', 'snehal_buldeo', 'astha._', '__the_gypsy_soul', 'mr_shutterr', 'this._.is._.abhi', 'soni.ankur608', 'meridharmarak', 'amanmundhada', 'jain_vipul_10', 'jn_ridhima_', 'adityadd10', 'aiiyan_sin', 'vipinv184', '_ayushi._.jain_', 'sagar.chandrakar.2112', 'the_small_town_guy', 'crystalmyth__', 'khushisahu_1819', 'arundeivam', 'mukeshmukundshukla', 's_r_a_hideout', 'srinivas_kumar5255', 'nitesh_sharma5292', 'ankitjangir001', 'eyelids_photography', 'saurav2303', 'k_chitra_rao', 'tanshi.rungta', 'vamsi_kolli', 'shreyansh_bohidar', 'darkphoenix_007', 'ritikks235', 'chandan_barik', 'classicshooter_', 'sunil_watti', '_karan_agrwl_', 'vaishnavy_ram', 'freshqo_tiffin_center', 'mackdcoool', 'the_world_in_b_w', 'kishna_frames', 'bhargavnaidutelagareddi', '_dishs_', 'manoranjan1403', 'rakesh.009', 'ray_priyanka_', 'msd.asish', 'ieeenitrr', 'raja_singht', 'rudra_fcb', 'saranya_amara121', 'j.denissen.photography', 'basudev_dalai', 'selfiesh_05', 'saqlain_shaikm', 'abhishek2kr', 'arshad.dhada', 'anurag_ec', 'evegyna', 'leehobbsroberts', 'dipesh_ranveer', 'rowdy_1107', 'taniya_bisen', 'sumit3662', '_nobby97_', 'rahul_svs', 'vermanishith', 'himanshu_shende_', 'buruguabhinav', 'samruddhi_wasnik', 'dhanendra_', 'janakirameyya', 'shreyansh3.9', 'sandeepsahu748', 'nsharmaz', 'assassin_kamal', 'itz_art3mis', 'shushriyaswarnkar', 'daivik_007', 'akhil_krishna_3', 'naitik_n.p', 'yash_raj_7', 'ramakant.patel', 'gunjan._.mishra', 'thalendrasahu', 'navi2804', 'jaanvi.d34', 'satyapraveen_24', 'theurbanguy_', 'neeraja_yalpala', 'pradeep_nayak30', 'aishwarya695', 'vishvaraj_', 'nukatejeswara', 'urstrulysuresh', 'dd0__026', 'dungaashritha', 'dixit.siddharth', 'anurag_chowdary7', '_kiru__panchal', 'madanmohant47', 'ved_om', 'prakhar_v03', 'kunjan.rajput', 'imranphotofilms', 'barenzimo', 'jagadeesh__mutra', 'vivek_kumar07s', '_p.jot_', 'rama_chandra_varma_uppalapati', 'kunvarsaheb', 'anupam_vikas11', 'seema_bh07', 'narendra_sonii', 'devil_6okro', '__ashrut', 'priya_singhania97', 'nikhileshagrawal711', 'they_call_me.photographer', 'c_a_t_c_h_e_r._', 'nxhnt', 'd_shishir', 'nazrine_kujur___naz_', '_alekhyaa_', 'hpincha', 'spandana.kancheti', 'jhootamemer', 'pushpendra_aneshwari', 'pixelpalsdigital', 'vyombani07', 'the_incredible_bharath', 'g24634553', 'devdasmanoj', 'lava_kumar3', 'akanksha_me19', 'ccnitrr', 'thegautamkr', 'abhishek.k.sarda', 'angelicshilpa', 'bhukya_pavan', 'nidhidewangan62', 'raj.banothu', 'sravyavaliveru', 'aesth_esicks', 'kumarpilla', 'sachinsarang1896', 'sanidhya1601', '_shashank_chandrakar_', 'bhavesh_sahu_1509', '_pandey.mic_', 'rjt_wildlife_photography', 'ankitakulkarni7', 'ayushinsights', 'sreejasingh_porika', 'shareguru5', 'pragya_nandan', 'piyush_tiwari__', 'the_bestco', 'satyendrasir', 'surendra_jm', 'rs_22.07', 'sagarkksrivastava', 'bollyshoots143', 'sanjeethdk', 'just_a_particle_of_dust', 'gopigarlapati27', 'sreekamal97', '_aymuos', 'mirrors_solenote', 'sab_badhiya_', 'rshemanth', '_kamlesh__01', 'adarsh_tiwari12', 'toothsome.tales.of.raipur', 'instatoshashi', 'mihir._.photography', '_amantiwary_', 'the._.white._.shadow', '_parimal_812', 'bhuwnshwr', 'rawbypoojabharti', 'itsme_kaushal', 'roshnipanda_', 'madhu_1998', 'mihir_m_pawar', 'abhishek.abhi010', 'ankit.rao.95', '_srigauri_', 'lemmatized_token', 'dimplesai23', 'mr_beardbaba', '__arjunnksyp', '_heli0s.__', 'kirtivardhanyadav', 'mani_476', 'raipur.student.things', 'naman_punia', 'khem__96', 'rishabhchouhan_22', 'saikiran.nagurla', 'nikitabuxy', 'gannu_009', 'vip_numberwale', 'santoshi1266', 'rohit_singh90831', 'arnodroaian', '_parvez_hayat_khan_phk__', 'sejal_ag119', 'dewangansumit96', 'ketan_puyad', 'medhaom', 'yogesh_snaps', 'mr._yashasvi', 'ehtramkhan', 'shalinee_kutare', '_ronin07_', '_adityanigam_', 'kartikeya40', 'ap_pratik96', 'fotoo_wala', '__harsh_agrawal__', 'sartorial_city_women', 'shailendra_bhimte', 'rashisahu515', 'star_gazer010', 'pati_ymn', 'lalith_naren', 'kaavya__n', 'rangillu_aashaavaal', 'bhilaieducationtrust', 'yadavankur8', 'rahulagrawal3845', 'neha__vishwakarma', 'thegeniecoach', 'amway_msg', 'pratap_nath_singh_', 'ankit_kmar', 'praveen.9312', 'palak19j', 'arham_chouradiya', 'rahul__karki', 'vaidhya_madhavan', 'harapriya_idr', 'nanda_in_exile', 'anshulekka', 'pallavidaharia7', 'the_sweet__weapon', 'udaykirandyda', 'shubham.bakshi.376', 'ak163496', 'afroznself1', 'priyam9990gupta', 'businneslivesupport', 'shristi02_', 'ujjawal__trivedi', 'sameer___tiwari', 'surbhirai98', 'kavita_18_', 'avishajaiswal', 'ar.jaypee', 'saycheesephoto_872', 'guptaaanchal3285', 'divijavaidya01', '_shreyashrivastava_', 'anonymous_15102', 'anushk_21', 's_a_m_.e_e_r._', 'inamdar_mihir', '_mamta_priya', 'amankhan9153', 'mus_kan5863', 'ajayawl', 'nadh_ghattamneni', 'rachana._.rotte', '_aparna11', 'jay_prakash02', 'madhu898', 'akramkhan7510', 'venky_myluru', 'raipurclicks', 'bhavesh9182', '_captured_moment__', 'vikram._xx', '_nishantchanda_', 'abhishekgupta1624', 'dileepkumar_seera', 'illustrationsby_anikesh', 'priyanshumohan9849', 'ashutosh__bagade__', 'anxious_morty', 'viveknag08', 'lav.kumarr', '_poetography', '_vanshika_v', 'sarvagya_210', '_rathi_ji_', 'sushantibhagat', 'unseen___pictures', 'iamkankit', 'tejpratap_007', 'foodlolyes', 'living_soul3938', 'click.by.me__', 'bhoomi_gajpal', 'durges__h', 'gupta_suyash1003', 'focus_paradox', 'vaib_photography', 'yashwantkothle', 'swanandagharkar', 'artmessenger1978', 'moonlight0195', '56th_byte', 'be_it_2804', 'sarita_nrityam', 'ash_ishrajak', 'ajaykr_kj000', 'shivani_kavitkar', 'its_kashyap_96', 'dima_cessna', 'comptesylviele', 'ice_geek96', 'akhi_1907', 'civiliansraipur', 'athishjadhav', 'bhai_to_bhai_che', 'ig_arsssh', 'srujica_addala', 'silent_knight3', 'devaraju_pilli', 'naivedyaj', 'ish.sri', 'viku_paswan', 'knowyourcolleges', 'nikhil_mandhania', 'reelkrish', 'bindhu653', 'dubisa0', 'hardikptel', '__________dev', 'vikram_shukla2000', 'ssaritasingh27', 'rishabh.singh111', '_p_hemanth_', 'mr.ramacharitikam', 'yashasva_paras', 'p.o.o.j.a.0304', 'shrivatsa_krishna', 'srai036', 'nitians.network', 'dewanganpranav', 'lovemouni19_dz', 'arushi16780', 'saicharanreddyyy', 'literary.nitrr', 'suyash_vairagade', 'akanksha10051998', 'oggy_babu', 'thakur.siddharth.singh', '__c.l.i.c.k.e.d__', 'krishnateja325', 'soni_anamika', 'mondler_0835', 'poonamsankhe', 'riya123singh2', 'amt_2048', 'i_m_mry7', 'sumit2674', 'prashant___kashyap', 'sta.r05', '_aysha_rauf', 'kuch.ahsaas', 'kumaresh.pillai', 'bambodesachin', 'i_t_s__v_k_', '_teman_singh', 'anglinapatel', 'mr.nick_hitler_2297', 'rahultripurana', 'im_naush', 'akhil0435', 'mona.funky', 'manjuyadav5563', 'pushpak_v_patil', 'nvdpkm', 'p_r_p_17', '_.rajatm2136._', 'kush_devansh', 'kavita7934', 'sardarsumana943', 'manas_ranjan_meher', 'cosmic_devesh', 'kosaria.gif', 'deepali.soni_', 'one8crew.ns', 'sahu_reema_', 'priyanka_kaja', 'ajitkumar2101', 'the_human_di_pod', '_aman_ranka_', 'durgeshjanghel27', 'ram_narayan_02', '_aniclicks_', 'yoo_brook1', 'mystique_shreya', 'jyoti_jrajput', 'sarandeeeep', 'meshram_shikha', 'mechneer_veteran', 'imvishesh007', 'gurudattdahare', 'adityab__', 'rangjalu_basumatary', 'lvusona', 'somesh_kashyap', 'ramesh_singh_rathod', 'suraj.g26', 'iso_at_800', 'mcreader_913', '_ravin_mourya', 'ashutoshdammani', 'kashyapkavala', 'adp_13', 'enarchin_dcreativeu', 'vi.pin962', 'pankaj._.kaushik', 'aditya_12_17', 'mayanks_27', 'ialokmishra', '__ayush.mishra_', 'fluid.mech.ii', 'naval_nkd', 'sandeepvkrm', 'explorecapture__', 'sahitya_singhania', 'rathi.prateek2', 'koduri_akhil', 'stoic_maxb', 'bhoibhoomi_', 'ved_tiwari', 'anamika31_', 'garvitgaba96', 'tarachandprajapati', 'disha_2502_', 'garotas_top6', 'jn_.ritika', 'its__leela__here', 'rupendrakumar15', 'ramesh_durga83', '_.sharu499._', 'prabhat_sukla', 'j0s3ph_z', 'ashwin_private', 'bhargav_hemanth', 'ra0_man0j', 'shalini_kashyap15', 'yaznesh_', 'praveengoldar', 'm__tushar', 'teja_kandada', 'akshar656', '1k.without.any.post', 'praveensatya21', 'navalksahu', 'khanchandiohaji', 'santoshm914', 'dheeraj__yadav09', 'pallavisom', 'vaidehi.mishra_', 'deepakumari297', 'iamshyamsinghrajput', 'sakshikalamkar', 'zayka.zindagi.ka', 'roy.siddharth06', 'singhpravin12', 'yashwantkot', '_ka_mi_ya', '_c_h_i_m_e_r_a__', 'avinash_g1', 'apoorva__3012', 'vinitbhinde', 'rajpootumeshsingh', 'the_nightmare_1990', 'ntsdwkr', 'kshitij._sharma', 'vivek.agrawal_', 'paridhi2135', '_kunal_chandrakar_', 'vivekkosuru', 'the_juluru_girl', 'suraj_shrma_', 'the_convocated', 'bohemian.monk', 'stylosubran', 'mrconsistent', 'memoriesphotography__', 'its_not_good_but_still_i_', 'piyush_2000', 'vinayshree_02', '_chhayasahu_', 'amanjain.15', 'aswathy_varma_', 'deepak_kumar_yadav78', 'vishnudewangan3', 'kavi_rai_28', 'prshant_kr', 'vuyyala_bhanu_prakash', '_naveeeen', 'amarjeetkumar2132', 'utopian_shiv_', 'iamiraman', '__imvr', 'sreedhar.g.reddy', 'iit_photos', '_.shumela_naz._', 'vidit_k9', 'the_venus_girl_', '_priyanshu_ap', 'wabi_sabi011', 'shubhkela', 'creat._.ve_snaps', 'bhavik___10', 'shwetimasakshi', 'irajatpradhan', 'wadhwani_harsh_', 'mohitt.sharmaa', '__niteesh', 'al562ex', '_______ayushi_______', 'ankit.254', 'jantakeboli', 's_amit_6910', 'akansha._agrawal', 'suryabhandhurwe', 'paras521985', 'mr_tushant_', 'clicksby_shivam', 'ashishsoni2802', 'pratiktolambia', 'kaman0807', 'prashant_gupta743', 'kntejasri_99', 'sumitmahato07', 'motivah_', '_ankurkunal_', 'prithvijitbose', 'nigga_higgga', 'meetliya', '_avi_n1', 'jeetujeetesh', '__k__kureti_15', 'arti12_09', 'aayushbhoi', 'neeraj_62', 'sabmohmaayahai_', 'shivam.agrawal12', 'tushardevsingh', 'hematilak', '_tushar_singh008', 'nishthathakre', 'shauryamanhar', 'the_chaigrapher', 'jagriti.thiske', 'shivam_2997', 'tuman_v_3003', 'proxygraphy', 'kamala_x180', 'chirag___0_0_7', 'rahulpatidar0506', 'imahendra.gavel', 'tomvarghese407', 'itzz_vibes_', 'apratimgauraha', 'shanmukha22', 'pratiksanjaywagh', 'robinhood.seeker', 'shreyash_royzada', 'kumawat10_', 'rinkudeegwal', 'sweet__being', 'lav_status777', '_vinayghritlahre_', 'arpan0710', 'arushi.anand.99', 'adityalucky44', 'meshramdipesh', 'photography_nature_jyoti.c6', 'kumarjhakeshav', 'shivendra_p_s_c', 'nihal_parkhedkar', 'the_abhay_agrawal', 'gajendra_paikra555', 'imagixpro', 's.t.u.d.e.n.t_h.u.b', 's_dub_projects', 'tanya_pachbiye', '__arjunkshyp', 'sayali_satdeve', 'poorvi_agrawal17', 'its_rajesh002', 'yuk_ta_ta', 'music_geek_2000', 'madhav.tumpati', '_adiii_11', 'yashchopra405', 'himanshu_kumar_agrawal', 'sakivinaw', 'mayank13sahu', 'manish.m27', 'rorschach_._', 'saksham_98_agrawal', 'aparnacmanoharan', 'being_collegiate', 'gurudattaishan', 'deveshdron', 'chromepipou', 'anjani_banjare_', 'mayank0982', 'its__abhi__singh', 'tulesh.15', 'ankit.singh0105', 'thesky.11', 'navyathomaz', 'choudhari_aman', 'mor_raipur7', 'varfo447', 'shail.yadav.1804', 'ar.damini8gupta', 'kunal_karunik', 'dprakash31', 'itsme_ketak', '_shriyakduggad_', 'palankita1804', 'ecell.nitraipur', 'asit_ks', 'sinha.gyanendra8301', 'shreeshreelaxmiclothing', 'sabhinav007', 'shubham.amraotkar', 'mr_cool_6.0', 'hotshotsnookerhub', 'agrawalsays', 'nitinkashyap3205', 'sravani_nagubandi', '37abhi', 'city_print_sai_promoters', 'uttarakhatik', 'thecarzwash', 'sinnibanjare', 'abigailrachelk7', 'harishkumarmiri', '_vitthal_', 'mat_maan__0903', 'jbs.suprim', '__homiii_06', 'jayprakash_nage', 'ashish_m15', 'littlemunchkinsdress', 'shinobi101_', 'drupeshkumar', 'goleshivam', 'rati_007', 'animesh_288', 'samirbajpai', 'ram_rhinestone', 'abhishekkumar2214', '_emmanuel_dinesh._', 'adweyta', 'i_shoot_people__', '_aakanksha.jha_', 'sravankumar_uppada', 'srbh1401', 'shruti.sehra', 'jiteshmurarka', 'samar.nitrr', 'swastiksahooo', 'iam12346814', 'aicandoanything', 'raj.s.makkad', 'sushil_prabhat', 'lakshyaapp', '_abhishek22_99', 'rajnish.cap_', 'gogreennitrr', 'mighty_munnu', 'simranjethanandani', 'srkram93', 'vineethjakkam', 'arnavmishra970', '_anjali_2803_', 'priyteshprasad', 'frarchitecturegallery', '_rahul_dhayal_', 'chandusampathirao', 'tusharsahu2115', 'pun_chami', '_floralclicks', 'wrapthefone', 'ishikajain_1705', 'amit_v06.12', '_._raj.thakur_._', 'myworld_lens', 'nikhillodhi', 'bhavesh_5_', '_iamanimesh', 'simran_bajaj._', 'sumona_ss', 'gauravpatel10', 'mhd.hisham.h', 'this__is__akshay', 'sonidevendra0', '_krishn123', 'russiannoobs', 'amar_dwivedi_', 'memer_nibbaa', 'tarak_gaurav', 'neerajmandare', 'tamra_333', '___rohith_sai___', 'beauty_of_raipur', 'nilaypandey_', 'sajaltiwari', 'nandudi8989', 'globetrotter_khush', 'vipul_ag2200', 'ahuti.mishra', 'shreyanshbafna', 'heathen.x_x', 'rohan_agrawal28', 'siddygupta', 'vivek_525', 'rheajaiswal24', 'rajsingh5560', 'aakash_s_18', 'clamorography_avi', 'pavinder133', 'mohnotyash', 'saurab2612', 'just_sarcastically', 'ragetechnology', 'the.sea.king', 'gulshan_verma46', 'ashwinipatle', 'roshankumar27706', 'imounish', 'nit_raipur', 'india_unrevealed', 'vamshi_rao_jupelli', 'lucky_lv0607', 'rsai11_sayings', 'suyashsinha1998', 'wanderer1227', 'abnvs', 'rishabhkothari19', 'vanshika_affiliate', 'reman_kumar_', 'deviprasad_gdp', 'imrankhan_pathan_', '_jyoti_30', 'roopanshpawar', 'aaditya__chaudhary', 'aiyushprasad', 'preeti.patel_', '__s_u_r_y_a_', 'ajay_2401', 'am_dkd', '_abhisheksingh17', 'bhasadd', 'd.scent_', 'g.mohitkumar', 'ashishkumarthakur174', 'behera.anjali0302', '_surjeet_231', '_purnima_07', 'ghumakkad.prani', 'kkskishore', 'mohitsharma_ontheway', 'dclick20', 'https.shubh', 'ayush._921', 'uncanny_soul', 'ec_raipur', 'prof_maulikjoshi', 'rock_readers', 'picturescape_', '_.zephryn._', 'siddiqfiroj', 'gagan_toppo', 'anu.rag.14', '21kshobhit', 'arushihihihi', 'kanishk_gabel', 'an0ushka._09', '_me_bhawesh_', 'manishmalhotra__', 'rishabhagrawal_', 'ashishgupta09oct.ak', 'ritesh.rv', 'toshendra.bohra', 'tony_parzival', 'gauravkridutt', 'nikita__nupur', 'jyotirmoy199', 'rath_150', 'breads_and_bucks', 'biharibhau', 'anshu.kumari04512018', 'i_am_a_happy_hippie', 's8a7b6', 'abhaya_shankar05', 'manisha_bisai_', 'sanchita__karmakar', 'kritik_dt', '_abhi_pratap', 'gunjeeta_09', 'you_know_who1067', 'yogesh_dewangan08', 'official_photographerz_world', 'ar.shubham.minocha', 'ayushi.yadav26', 'cake_o_lecious_', 'they_callme_sway', 'm_o_h_i_t_p_d', 'rajan_xz', 'arpit.__.jain', 'komadikesh', 'v_aish.mehar_', 'rk_atishay', 'sanket.patra', 'robotix_nitrr', 'etherealcrm', 'tshivansh44', 'sameerranjan009', 'guptakuhu', 'bhuvana_sekhar_reddy', 'vanshika_1631_', 'pu9t', 'howabegam', '__vinash__14', 'sanjana_tiwari20', 'ashishv_02', 'ajaygpta', 'divya_emily', 'jools.tv', 'shraddha.biyani', 'vinaychauchan08', 'amrit_1399', 'ayush_tiwari_1201', '_rahul_rathore__', 'visheshtiwari02', 'revanth.tellabati', 'sankalp44', 'pentakota_naveen_kumar', 'prym195', 'apar_na_gupta__', 'sagarkumarbhagwani', 'stfuavneesh', 'mayanknagle', 'akhil_2772', 'innovation_cell.nitrr', 'emric_nihal', 'hemant_r27', 'be_creative_21', 'lavjaiswalmgj', 'surbhi_agrwl', '_aman.agrawal._', 'chikkyreddie', 'dhairyachandrakar', 'my3682233', 'saketpandey_', 'kash_less_', 'govind_sahu143', 'raastewithrajat', 'vineet_mm', 'paraspatel05', 'nirmitsaa', 'pujasahu899', 'snehall___', '_shreya_2212', 'syed_0123', 'g.s__09_']
            for entry in mylist:
                if request.POST['Username']==entry:
                    messages.success(request, "You are following clickclubnitrr")
                    return redirect('quiz')
            
            messages.warning(request, "You are not following clickclubnitrr")
            return render(request, 'index.html', {'form' : form})
    else:
        form = UserForm()
    return render(request, 'index.html', {'form' : form})

def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request, 'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request, 'quiz.html',context)

def profile(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request, 'profile.html',context)

def userprofile(request,pk):
    allposts = Post.objects.all()
    User = get_user_model()
    postuser = get_object_or_404(User, pk=pk)
    if request.user==postuser:
        return redirect('profile')
    context = {'allposts':allposts,'postuser':postuser}
    return render(request, 'userprofile.html',context)

def about(request):
    return render(request, 'about.html')

def mypost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    User = get_user_model()
    allusers = User.objects.all()
    context = {'allusers':allusers,'post': post}
    return render(request, 'mypost.html', context)

def addQuestion(request):    
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user != post.user:
        next = request.GET.get('next', reverse('mypost',kwargs={'pk': pk}))
        return redirect(next)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been edited")
            next = request.GET.get('next', reverse('mypost', kwargs={'pk': pk}))
            return redirect(next)
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)
    return render(request, 'editpost.html', {'form':form, 'post':post})

def userlogin(request):
    return render(request, 'login.html')

def usersignup(request):
    return render(request, 'signup.html')

def handlesignup(request):
    if request.method == 'POST':
        #post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #check for incorrect inputs

        if len(username)>20:
            messages.error(request, "Username cannot exceed 20 characters")
            return redirect('usersignup')

        if not username.isalnum():
            messages.error(request, "Username must contain only letters and numbers")
            return redirect('usersignup')

        if password!=confirm_password:
            messages.error(request, "Incorrect password")
            return redirect('usersignup')

        #create user
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You have successfully created your account!")
        return redirect('home')
    else:
        return HttpResponse("404 not found")

def handlelogin(request):
    if request.method == 'POST':
        lusername = request.POST['loginusername']
        lpassword = request.POST['loginpassword']

        user = authenticate(username=lusername, password=lpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"You have succesfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again!")
            return redirect('userlogin')

def handlelogout(request):
    logout(request)
    messages.success(request, "You have been successfully Logged out!")
    return redirect('home')

def deletepost(request,id):
    post_to_delete=Post.objects.get(id=id)
    post_to_delete.delete()
    messages.success(request, "Your post has been deleted successfully!")
    return redirect('home')