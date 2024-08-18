def convert_number_systems(num, base):
    try:
        if base == 2:
            num = int(num, 2)
        elif base == 8:
            num = int(num, 8)
        elif base == 10:
            num = int(num)
        elif base == 16:
            num = int(num, 16)
        else:
            raise ValueError("不支持的进制")
        
        return {
            "二进制": bin(num)[2:],
            "八进制": oct(num)[2:],
            "十进制": num,
            "十六进制": hex(num)[2:]
        }
    except ValueError as e:
        return str(e)

def main():
    try:
        _2_num = input("请输入二进制数字：")
        _8_num = input("请输入八进制数字：")
        _10_num = input("请输入十进制数字：")
        _16_num = input("请输入十六进制数字：")

        results = {
            "二进制": convert_number_systems(_2_num, 2),
            "八进制": convert_number_systems(_8_num, 8),
            "十进制": convert_number_systems(_10_num, 10),
            "十六进制": convert_number_systems(_16_num, 16)
        }

        for key, value in results.items():
            if isinstance(value, dict):
                print(f"{key}数字：")
                for k, v in value.items():
                    print(f"{k}: {v}")
            # else:
            #     print(f"{key}数字输入错误：{value}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
