class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n=len(code)
        ans=[]
        for i in range(n):
            if not isActive[i]:
                continue
            if businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                continue
            if code[i] and all(char.isalnum() or char == '_' for char in code[i]):
                ans.append(code[i])
        return ans



class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans = []
        valid_business_lines = {"electronics", "grocery", "pharmacy", "restaurant"}

        # zip bundles the three lists. Each loop iteration gives one element from each.
        # e.g., (code_str, business_str, is_active_bool)
        for current_code, current_business, current_active_status in zip(code, businessLine, isActive):
            
            # Condition 1: Must be active
            if not current_active_status:
                continue

            # Condition 2: Must be a valid business line
            if current_business not in valid_business_lines:
                continue

            # Condition 3: Code format must be valid
            if current_code and all(char.isalnum() or char == '_' for char in current_code):
                ans.append(current_code)
        
        return ans

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        # --- Step 1: Filter for valid coupons, storing the necessary info for sorting ---
        
        valid_coupons_with_info = []
        valid_business_lines = {"electronics", "grocery", "pharmacy", "restaurant"}

        for current_code, current_business, current_active_status in zip(code, businessLine, isActive):
            
            # Combine all validation checks
            is_active = current_active_status
            is_valid_business = current_business in valid_business_lines
            is_valid_format = current_code and all(char.isalnum() or char == '_' for char in current_code)

            if is_active and is_valid_business and is_valid_format:
                # Store the tuple (businessLine, code) for sorting later
                valid_coupons_with_info.append((current_business, current_code))
        
        # --- Step 2: Sort the filtered list using a custom multi-level key ---

        # Create a map to define the custom sorting order for business lines
        business_order_map = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        # The key=lambda function tells sorted() how to evaluate each item.
        # It creates a new tuple (sort_order, code_string) for comparison.
        # Python will sort by the first element, then by the second for ties.
        sorted_coupons = sorted(
            valid_coupons_with_info, 
            key=lambda coupon: (business_order_map[coupon[0]], coupon[1])
        )
        
        # --- Step 3: Extract just the codes from the sorted list ---
        
        final_sorted_codes = [coupon_code for business_line, coupon_code in sorted_coupons]
        
        return final_sorted_codes


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        category = ["electronics", "grocery", "pharmacy", "restaurant"]
        res = []
        for i in range(len(code)):
            if code[i].isalnum() or "_" in code[i]:
                if businessLine[i] in category:
                    if isActive[i]:
                        res.append([businessLine[i],code[i]])
        res = sorted(res)
        newres = []
        for i in res:
            newres.append(i[1])
        return newres