import { DrawerContentScrollView, DrawerItemList ,DrawerItem ,  } from "@react-navigation/drawer";
import { Linking ,View ,Image } from "react-native";

export default function CustomDrawerContent(props:any) {
    const image = require('../assets/images/logo.png')

	return (
	  <DrawerContentScrollView {...props}>
		<View style={{flexDirection:'row',justifyContent:'center'}}>
			<Image source={image} style={{height:200,width:200}} />
		</View>
		<DrawerItemList {...props} />
	  </DrawerContentScrollView>
	);
}