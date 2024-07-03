import { Text ,View } from "react-native";
import { StyleSheet } from "react-native";

export default function About() {
	return(
		<View style={style.view}>
			<Text>This APP Was Created By</Text>
			<Text style={{fontStyle:"italic"}}>El Mhadji Mohamed Abdelhake</Text>
		</View>
	)
}

const style = StyleSheet.create({
	view:{
		flex:1,
		justifyContent:'center',
		alignItems:'center',
	},

})
