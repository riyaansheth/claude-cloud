"""Common US given names — a validation dictionary, not lead data. A regex-found
"name" is accepted only when its first word is a known given name; anything else
(e.g. "Emeritus Board", "Assistant Sales") is left for the subagent pass."""
FIRST_NAMES = set("""
aaron abby abigail adam adele adrian adriana adrienne aileen aimee alan alana albert alberto
alex alexa alexander alexandra alexis alfred ali alice alicia alison allan allen allison alma
alvin amanda amber amelia amir amit amy ana andre andrea andres andrew andy angel angela angelica
angelo angie anita ann anna anne annette annie anthony antoinette antonio april ari ariel arlene
armando arnold arthur ashley audrey austin avi barbara barry beatrice becky belinda ben benjamin
bernadette bernard bert beth bethany betty beverly bill billy blake bob bobby bonnie boris brad
bradley brandon brenda brendan brett brian bridget brittany brooke bruce bruno bryan byron caleb
camille candace cara carl carla carlos carmen carol caroline carolyn carrie casey cassandra
catherine cathy cecilia celia chad charlene charles charlie charlotte chase chelsea cheryl chris
christian christina christine christopher cindy claire clara clarence claudia clifford clint
colin colleen connie constance corey cory courtney craig cristina crystal curtis cynthia daisy
dale dalia dan dana daniel daniela danielle danny darlene darren dave david dawn dean deanna
debbie deborah debra denise dennis derek diana diane dina dominic don donald donna dora doris
dorothy doug douglas drew dustin dylan earl ed eddie edgar edith edward edwin eileen elaine
eleanor elena eli elias elijah elizabeth ella ellen elliot elsa emil emily emma eric erica erik
erin ernest esther ethan eugene eva evan eve evelyn ezra faith felicia felix fernando fiona
frances francesca francis francisco frank franklin fred frederick gabriel gabriela gabrielle
gail gary gavin gene george georgia gerald geraldine gina giovanni gladys glen glenn gloria
gordon grace graham greg gregory gretchen hal haley hannah harold harriet harry harvey hassan
hazel heather hector heidi helen henry herbert holly howard hugh ian ilana irene iris irving
isaac isabel isabella ivan jack jackie jackson jacob jacqueline jaime jake james jamie jan jane
janet janice jared jasmine jason javier jay jean jeanette jeff jeffrey jenna jennifer jenny
jeremy jerome jerry jesse jessica jesus jill jim jimmy jo joan joann joanna joanne jodi joe joel
johanna john johnny jon jonathan jordan jorge jose joseph josephine josh joshua joy joyce juan
judith judy julia julian julie june justin kara karen kari karina karl kate katherine kathleen
kathryn kathy katie kay keith kelly ken kenneth kent kerry kevin kim kimberly kirk kristen
kristin kristina kurt kyle lance larry laura lauren laurie lawrence leah lee leo leon leonard
leslie levi lewis liam lila lillian lily linda lindsay lindsey lisa liz logan lois lori lorraine
louis louise lucas lucia lucy luis luke lydia lynn mackenzie madeline madison maggie malcolm
manuel marc marcia marco marcus margaret margarita maria marian marie marilyn mario marion
marisa mark marlene marsha marshall martha martin marvin mary matt matthew maureen max maxine
maya megan meghan melanie melinda melissa melvin meredith mia micah michael michele michelle
miguel mike mildred miles miriam mitchell molly monica morgan moshe muriel murray nadia nancy
naomi natalie nathan nathaniel neal neil nelson nicholas nick nicole nina noah noel nora norma
norman olga olivia omar oscar owen paige pamela patricia patrick patty paul paula pauline pearl
peggy penny perry pete peter philip phillip phyllis rachel rafael ralph ramon randall randy
raquel ray raymond rebecca regina reginald rena renee rhonda ricardo richard rick ricky rita rob
robert roberta roberto robin rochelle rodney roger roland ron ronald rosa rose rosemary ross roy
ruben ruby russell ruth ryan sabrina sally sam samantha samuel sandra sandy sara sarah scott
sean sergio seth shane shannon sharon shawn sheila shelley sherry shirley sidney simon sofia
sonia sophia stacy stanley stella stephanie stephen steve steven stuart sue susan suzanne sylvia
tamara tammy tanya tara ted teresa terri terry theodore theresa thomas tiffany tim timothy tina
todd tom tommy toni tony tracy travis trevor troy tyler valerie vanessa vera veronica victor
victoria vincent viola violet virginia vivian walter wanda warren wayne wendy wesley whitney
william willie wilson yolanda yvonne zachary zoe
aram armen arsen artur ashot avraham baruch chaim dov eitan eli gil hagop haim isaac levon
meir menachem mordechai nissim raffi sami shlomo tigran vahe yaakov yair yosef yossi zev
ahmad ali amin farid hamid hossein jamal karim mehdi mohammad reza saeed sami tariq yusuf
anh binh duc hoa hung khanh linh long minh nam ngoc phuong quang thanh thao tuan vinh
chen hui jun li lin mei ming wei xin yan ying yu
anil arjun deepak kiran manish neha nikhil pooja priya rahul raj rajesh ravi rohit sanjay
sunil vijay vikram
""".split())
