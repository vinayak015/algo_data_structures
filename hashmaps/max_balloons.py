"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        to_match = "balloon"
        frequency_map = {}
        unq = set(to_match)
        for char in text:
            if char in unq:
                frequency_map[char] = frequency_map.get(char, 0) + 1
        return min(frequency_map.get("b", 0), frequency_map.get("a", 0), frequency_map.get("l", 0)//2, frequency_map.get("o", 0)//2, frequency_map.get("n", 0))

        ##### is possible? #####
        # if unq - set(frequency_map.keys()):
        #     return 0
        #
        #
        # m = len(text)
        # l_count = frequency_map.get("l", 0)
        # o_count = frequency_map.get("o", 0)
        # min_double_count = min(l_count, o_count)
        #
        # for char in frequency_map:
        #     count = frequency_map[char]
        #     if char == "l" or char == "o":
        #         continue
        #     m = min(m, count)
        # if m * 2 <= min_double_count:
        #     total = m
        # else:
        #     # if m < min_double_count:
        #     total = min_double_count // 2
        #
        # return  total






if __name__ == "__main__":
    sol = Solution()
    text = "nllbblooon"
    text = "nlaebolko"
    # text = "balllllllllllloooooooooon"
    text = "loonbalxballpoon"
    text = "nllbblooon"
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    text = "mbetypbpefxvviadqaodrbjeoacfomepmzymiudltgnvnpbowwmjgpzzhtiismearuwocsgbiimiqqzaozgeizikrlxmupfzjzmlfttqqbpfblqfkecsdfbsceqjhubfxksivrfwvukapxmuciybfhzlmpeamdxziptxregymqtmgcsujmugissgnlbhxbcxxeoumcqyulvahuianbaaxgzrtmshjguqdaxvxndzoqvwmcjfhpevavnrciqbymnlylbrfkkiceienoarfrzzxtuaqapaeqeqolozadmtgjyhfqzpuaskjuawxqkdqyjqcmbxtvshzrquvegcuyuckznspmrxvqdassidcmrajedsnuuumfwqzvasljlyvfefktiqgvzvdzojtjegsyhbepdkuwvgrfscezvswywmdavpxlekbrlkfnbyvlobazmvgulxrfdranuhomkrlpbfeagfxxxuhjuqhbkhznixquxrxngwimdxdhqbdaouitsvcdmbwxbbaomkgxsqwnexbjjyhtxvkjfqkrrxjghvzqsattubphryqxxdyjkihfnzvjhohnhdlfwoqiwtmwzfgcyhyqtcketvgnbchcxvnhcsoosirfqgdgcsitegzlxdfijzmxnvhrulmgvoqfpzesootscnxenokmmozmoxpaverydbsnimwacjqhrtxkqtvghjyushoctxphxzztukgmnoeycqaeukymvwxcsyvvctflqjhtcvjtxncuvhkptkjnzaetwbzkwnseovewuhpkaxiphdicgacszzdturzgjkzwgkmzzavykancvvzaafgzjhcyicorrblmhsnnkhfkujttbkuuedhwguuaapojmnjdfytdhrepjwcddzsoeutlbbljlikghxefgbqenwamanikmynjcupqpdjnhldaixwygcvsgdkzszmsptqqnroflgozblygtiyaxudwmooiviqcosjfksnevultrf"
    print(sol.maxNumberOfBalloons(text))

