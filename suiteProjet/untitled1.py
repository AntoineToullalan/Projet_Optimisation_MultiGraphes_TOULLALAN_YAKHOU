from matplotlib import pyplot
from math import log,exp


l1=[-6.436751745449444, -6.279085586266082, -4.954904993666638, -3.6209626516974507, -3.0782755396355084, -2.250752617323066, -1.7281642489322413, -1.332294019752298, -0.0670121285204245, -0.022170993054222175, -0.2006425094851391, 0.1735969861859702, 0.35481903197262926, 1.1469965896334258, 1.1280503496867988, 1.1994923526555352, 1.327118517911646, 1.6664511500811474]
l2=[-10.20066483888215, -9.334114658467538, -8.189105012915777, -7.732913489252012, -7.3305365414211225, -6.582315288709264, -6.29886074979536, -5.331265829781715, -4.324447632956067, -3.988614566033006, -4.598792366596427, -4.505740480466178, -4.067394895335405, -3.248606493989828, -2.788821602572394, -4.268801087750819, -4.9117820825355025, -4.194744941833228]
l3=[0.6931471805599453, 1.9459101490553132, 2.4849066497880004, 2.833213344056216, 3.091042453358316, 3.295836866004329, 3.4657359027997265, 3.6109179126442243, 3.7376696182833684, 3.8501476017100584, 3.9512437185814275, 4.04305126783455, 4.127134385045092, 4.204692619390966, 4.276666119016055, 4.343805421853684, 4.406719247264253, 4.465908118654584]

#l1=[-3.4631650525541042, -2.1413455966197437, -0.7155519702242259, -0.6360504130682682, -0.19449951880100108, -0.004798031242392066, 0.41407080508700395, 0.583943212828888, 0.766081332249396, 0.9811645206138397]
#l2=[-8.200677816745639, -6.950598879882962, -5.176978580535797, -4.740899077142852, -4.313940546260774, -3.9096854229317657, -3.51775224326717, -3.3144085931871023, -3.194932848594139, -2.989212322567182]
#l3=[-2.3025850929940455, -1.6094379124341003, -1.203972804325936, -0.916290731874155, -0.6931471805599453, -0.5108256237659905, -0.3566749439387323, -0.2231435513142097, -0.10536051565782628, 0.0]

#l1=[-6.392406134082036, -6.102135634147201, -4.837662540220671, -4.092730341485716, -3.147646229419442, -1.9880626688793546, -1.6276085665735618, -0.4760410285341493, -0.11032397241404442, 0.16360030480195206, 0.3623365107300352, 0.9232257998980141, 0.37904581120186676, 0.6934728549850409, 0.8706095831582603, 0.9857626400126039, 1.4218446760369727, 1.2941250218869274, 1.6978794294378736, 1.873746273036024, 2.0244568275442143, 1.9566116822554391, 2.0249087951612297, 2.1115901436965587, 2.556873931084, 2.52191601513486, 2.652907907893219, 2.862977368913613, 2.918130416539701, 2.9618042800861732]
#l2=[-10.20969133472812, -9.135113412474928, -8.827940960654356, -8.016071404074872, -7.421279624642589, -6.647115570117254, -5.938708433087279, -4.855533708273234, -4.481709228827765, -4.434339575214475, -3.715919858071165, -2.790870046367158, -3.8337246948238994, -3.481093711041949, -3.8154574514657633, -3.06836621853096, -2.7423099051699533, -5.013623323913197, -4.502546643016045, -4.244006373524036, -3.7838402686838712, -3.531494243135154, -3.0030565465452153, -4.258205819312342, -4.016947469116416, -3.435255775734029, -3.48040597228121, -3.0453677503438232, -2.4910282922860345, -2.348604146397796]
#l3=[0.6931471805599453, 1.9459101490553132, 2.4849066497880004, 2.833213344056216, 3.091042453358316, 3.295836866004329, 3.4657359027997265, 3.6109179126442243, 3.7376696182833684, 3.8501476017100584, 3.9512437185814275, 4.04305126783455, 4.127134385045092, 4.204692619390966, 4.276666119016055, 4.343805421853684, 4.406719247264253, 4.465908118654584, 4.5217885770490405, 4.574710978503383, 4.624972813284271, 4.672828834461906, 4.718498871295094, 4.762173934797756, 4.804021044733257, 4.844187086458591, 4.882801922586371, 4.919980925828125, 4.955827057601261, 4.990432586778736]

#l2=[-8.124961018331337, -6.580934432488181, -7.227489302630247, -5.989191189388829, -5.320789550493417, -4.677084858448761, -3.8886379788823584, -3.239457773562484, -2.7123829072340686, -4.580305833727471, -4.188497829701459, -3.400586084491598, -3.1499796765290378, -4.463551774976289, -3.754895353879876, -2.948368346830633, -2.478998482068927, -1.7112731996467214, -0.43883740066026944, -0.4675726189568404, -0.44139282108427436, -0.44066010280065215, 0.24279624883396836, 0.0031136625324418503]
#l1=[2.302585092994046, 2.995732273553991, 3.4011973816621555, 3.6888794541139363, 3.912023005428146, 4.0943445622221, 4.248495242049359, 4.382026634673881, 4.499809670330265, 4.605170185988092, 4.700480365792417, 4.787491742782046, 4.867534450455582, 4.941642422609304, 5.0106352940962555, 5.075173815233827, 5.135798437050262, 5.19295685089021, 5.247024072160486, 5.298317366548036, 5.3471075307174685, 5.393627546352362, 5.438079308923196, 5.480638923341991]

#l2=[-8.981089106968575, -7.624130824079897, -7.458231815540705, -6.377697543973005, -7.10412346999309, -6.80128768364472, -5.901878546684526, -5.8008457322952856, -4.160368102691596, -4.7930082007904184, -4.725100010058674, -4.069033787610628, -3.7556992211487583, -3.6162520669481446, -3.1578287023985916, -2.8271370289600144, -3.1280058799041357, -2.4310777249070004, -4.909360129439562, -4.490596003117686, -3.9948921923798166, -3.7926580163910524, -3.464214995756432, -3.5069403938633377, -3.534125008269406, -4.584518279763192, -4.575844764898163, -3.69030478200285, -3.8747042638572617, -3.604641907425436, -3.120513542867297, -2.819266061098468, -2.3376079719853413, -2.2861282729176295, -2.090337768627123, -1.7854592385222228, -1.721504824684148, -1.700787260832376, -1.306978911101459, -1.015047343112171, -0.9746021151700551, -0.986937877967086, -1.0503082078018302, -0.5287286979899977, -0.47570585307567786, -0.40807845831818024, -0.2771405218719916, -0.35331949088417686]
#l1=[2.302585092994046, 2.70805020110221, 2.995732273553991, 3.2188758248682006, 3.4011973816621555, 3.5553480614894135, 3.6888794541139363, 3.8066624897703196, 3.912023005428146, 4.007333185232471, 4.0943445622221, 4.174387269895637, 4.248495242049359, 4.31748811353631, 4.382026634673881, 4.442651256490317, 4.499809670330265, 4.553876891600541, 4.605170185988092, 4.653960350157523, 4.700480365792417, 4.74493212836325, 4.787491742782046, 4.8283137373023015, 4.867534450455582, 4.90527477843843, 4.941642422609304, 4.976733742420574, 5.0106352940962555, 5.043425116919247, 5.075173815233827, 5.10594547390058, 5.135798437050262, 5.1647859739235145, 5.19295685089021, 5.220355825078324, 5.247024072160486, 5.272999558563747, 5.298317366548036, 5.3230099791384085, 5.3471075307174685, 5.3706380281276624, 5.393627546352362, 5.41610040220442, 5.438079308923196, 5.459585514144159, 5.480638923341991, 5.501258210544727]

#l2=[-1.2365648652482593, -0.7436449251674224, -0.5971092003492724, -0.5987728846907153, -0.41953876285559943, -0.3860963635055216, -0.46008989749448853, -0.3784989057233655, 0.4159418576463958, -0.22068778816645104, -0.3707880729434709, -0.4275321779564599, -0.29916473819785844, -0.3620705130885096, -0.33463007667504013, -0.41690506721774767, -0.2518124298609198, -0.36287548692622174, -0.32100620952349607]
#l1=[2.302585092994046, 2.995732273553991, 3.4011973816621555, 3.6888794541139363, 3.912023005428146, 4.0943445622221, 4.248495242049359, 4.382026634673881, 4.499809670330265, 4.605170185988092, 4.700480365792417, 4.787491742782046, 4.867534450455582, 4.941642422609304, 5.0106352940962555, 5.075173815233827, 5.135798437050262, 5.19295685089021, 5.247024072160486]

#l2=[-1.2315523737144674, -1.0206442309418386, -0.8684002531208758, -0.6317909655329889, -0.484402373417541, -0.6030024140100267, -0.5313559069825187, -0.49102359952875174, -0.49245620888692615, -0.465954335964297, -0.4288989293290889, -0.5552712687515414, -0.425171132862268, -0.2872470531795263, -0.3271917652422118, -0.42502971291550107, -0.29294324267572547, -0.2828842209928153]
#l1=[2.302585092994046, 2.70805020110221, 2.995732273553991, 3.2188758248682006, 3.4011973816621555, 3.5553480614894135, 3.6888794541139363, 3.8066624897703196, 3.912023005428146, 4.007333185232471, 4.0943445622221, 4.174387269895637, 4.248495242049359, 4.31748811353631, 4.382026634673881, 4.442651256490317, 4.499809670330265, 4.553876891600541]

#l2=[-5.00597115740396, -4.619192641378487, -3.575584931366872, -2.8654533360724224, -2.2281706041034006, -1.6594608791010268, -1.2490644341662933, -0.531925033589395, -0.0014580980500195667, 0.1595858925610512, 0.43760661452134136, 0.16005737467181713, 0.2598251043104637, 0.8055861678385894, 0.6856119849625887, 0.8220609437690128, 0.9643883114150331, 1.1044812890376257, 1.3166865521282012, 1.4486558396857265, 1.490210988216308, 2.060981226994676, 1.721410987078307, 2.1687239267291942, 1.9796391383436236, 2.1642215544511236, 2.2288583390800443, 2.4538920829385313]
#l1=[2.302585092994046, 2.70805020110221, 2.995732273553991, 3.2188758248682006, 3.4011973816621555, 3.5553480614894135, 3.6888794541139363, 3.8066624897703196, 3.912023005428146, 4.007333185232471, 4.0943445622221, 4.174387269895637, 4.248495242049359, 4.31748811353631, 4.382026634673881, 4.442651256490317, 4.499809670330265, 4.553876891600541, 4.605170185988092, 4.653960350157523, 4.700480365792417, 4.74493212836325, 4.787491742782046, 4.8283137373023015, 4.867534450455582, 4.90527477843843, 4.941642422609304, 4.976733742420574]


#l2=[-3.6523666576232934, -2.3702540173614164, -1.4481943070345755, -0.5885690553547502, 0.312012068964841, 0.2967325491241587, 0.18452974395268326, 0.03944984154317845, 0.43500999401503665]
#l1=[-2.3025850929940455, -1.6094379124341003, -1.203972804325936, -0.916290731874155, -0.6931471805599453, -0.5108256237659905, -0.3566749439387323, -0.2231435513142097, -0.10536051565782628]


pyplot.figure()
pyplot.plot(l3,l1,'red',label="Avec Guroby (Q5)")
pyplot.plot(l3,l2,'blue',label="Sans Guroby (Q4)")
pyplot.xlabel("log p")
pyplot.ylabel("log Temps de calcul ")
pyplot.legend()
pyplot.show()