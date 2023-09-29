import { 
	StyleSheet, 
	Text, 
	View 
} from 'react-native'
import IonIcons from '@expo/vector-icons/FontAwesome'


const Label = (props) => {
  return (
	<View style={{flexDirection:'row' ,alignItems:'center' ,justifyContent:'center'}}>
		<IonIcons
			name={props.name}
			size={30}
			/>
	 	<Text
			style={{fontSize:20 ,paddingLeft:5}}
			>
			{props.label}
		</Text>
	</View>
  )
}

export default Label

const styles = StyleSheet.create({})