#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  useEffect(() => {
+    const handler = e => {
+      if (e.key === 'Escape') {
+        fn();
+      }
+    };
+    window.addEventListener('keydown
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  const unload = e => {
+    e.preventDefault();
+    e.returnValue = '',
+    fn();
+  };
+  window.addEventListener('beforeunload', unload);
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+    const unloadHandler = (event) => {
+        event.preventDefault();
+        event.returnValue = 'Are you sure you want to leave this page?';
+        return 'Are you sure you want to
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  React.useEffect(() => {
+    window.addEventListener('beforeunload', fn);
+    return () => {
+      window.removeEventListener('beforeunload', fn);
+    };
+ 
```

#### useUnload (task/1)

```diff
-const useUnload = fn => {
+const useUnload = fn => {
+
+  const [, forceUpdate] = useState(null);
+  useEffect(() => {
+    window.addEventListener('beforeunload', fn);
+    return () => {
+      window.removeEventListener
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    useEffect(() => {
+        const handleClickOutside = (event) => {
+            if (ref.current && !ref.current.contains(event.target)) {
+                callback();
+            }
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+  const handleClick = e => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback()
+    }
+  }
+
+  useEffect(() => {
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+  useEffect(() => {
+    const handler = event => {
+      if (!ref.current || ref.current.contains(event.target)) {
+        return;
+      }
+      callback();
+   
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+  useEffect(() => {
+    const handleClickOutside = event => {
+      if (ref.current && !ref.current.contains(event.target)) {
+        callback();
+      }
+    };
```

#### useClickOutside (task/2)

```diff
-const useClickOutside = (ref, callback) => {
+const useClickOutside = (ref, callback) => {
+
+    const clickHandler = event => {
+        if (ref.current && !ref.current.contains(event.target)) {
+            callback();
+        }
+    };
+
+    useEffect(() => {
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    try {
+      const item = sessionStorage.getItem(keyName);
+      return item ? JSON.parse(item) : defaultValue;
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const [storedValue, setStoredValue] = useState(() => {
+    try {
+      const item = window.sessionStorage.getItem(keyName);
+      return item ? JSON.parse(
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    const stored = sessionStorage.getItem(keyName);
+    return stored ? JSON.parse(stored) : defaultValue;
+  });
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const value = sessionStorage.getItem(keyName);
+  if (value === null) {
+    sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
+    return defaultValue;
```

#### useSessionStorage (task/3)

```diff
-const useSessionStorage = (keyName, defaultValue) => {
+const useSessionStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    const value = sessionStorage.getItem(keyName);
+    return value === null ? defaultValue : value;
+  });
+
+  const set
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  useEffect(() => {
+    document.title = title;
+  }, [title]);
+};
+
+const useTheme = () => {
+  const [theme, setTheme] = useState(null);
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+    useEffect(() => {
+        document.title = title;
+    }, [title]);
+};
+
+export default useTitle;
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  useEffect(() => {
+    document.title = title;
+  }, [title]);
+};
+
+const toggle = (toggled, click) => {
+  if (toggled) {
+   
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+  useEffect(() => {
+    document.title = title;
+  }, [title]);
+};
+
+const useFetch = (url, init) => {
+  const [response, setResponse] = use
```

#### useTitle (task/4)

```diff
-const useTitle = title => {
+const useTitle = title => {
+
+	const [pageTitle, setPageTitle] = useState(title);
+	useEffect(() => {
+		document.title = `${pageTitle} | Echterhoff.dev`;
+	},
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  const mounted = useRef(false);
+  useEffect(() => {
+    if (mounted.current) return;
+    mounted.current = true;
+    callback();
+  }, [when]);
+};
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+    const didRun = useRef(false);
+
+    useEffect(() => {
+        if (didRun.current) return;
+        didRun.current = true;
+        return callback();
+    }, when);
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  useEffect(callback, [], when);
+};
+
+export default useEffectOnce;
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  const active = useRef(true);
+
+  useEffect(() => {
+    if (active.current) {
+      when && callback();
+      active.current = false;
+    }
+  }, [when
```

#### useEffectOnce (task/5)

```diff
-const useEffectOnce = (callback, when) => {
+const useEffectOnce = (callback, when) => {
+
+  useEffect(callback, [when]);
+};
+
+const useMounted = () => {
+  const [mounted, setMounted] = useState(false);
+  useEffectOnce(() => {
+   
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const iconClass = isCollapsed ? 'icon-plus' : 'icon-minus';
+  return (
+    <li>
+      <div onClick={handleClick} className={classNames({ 'accord
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const itemClass = isCollapsed ? "collapsed" : "";
+  return (
+    <div className={`accordion-item ${itemClass}`}>
+      <button className="acc
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const handleToggle = (event) => {
+    event.preventDefault();
+    handleClick(label);
+  };
+
+  return (
+    <>
+      <h4 className="accordion
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const [isActive, setIsActive] = useState(false);
+
+  const toggle = () => {
+    setIsActive(!isActive);
+  };
+
+  return (
+    <AccordionItem
```

#### Accordion (task/6)

```diff
-const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
+
+  const buttonClass = isCollapsed ? 'button collapsed' : 'button';
+  return (
+    <div className="accordion-item">
+      <button className={buttonClass} onClick={handle
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' && (window as any).document ? React.useLayoutEffect : React.useEffect;
+
+const createCtx = <T>(defaultValue: T): [T, React.Dispatch
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect
+
+const PREFIX = 'inline-block'
+
+export interface InlineBlockProps {
+  className?: string
+ 
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? useEffect : useLayoutEffect;
+
+export function useEvent(eventName: string, handler: EventHandler, options?: EventOptions): void {
+  useIsomorphicEffect(()
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' ? React.useLayoutEffect : React.useEffect
+
+function getOuterSizes(node: HTMLElement) {
+  const size = {
+    width: node.
```

#### useIsomporphicEffect (task/7)

```diff
-const useIsomorphicEffect =
+const useIsomorphicEffect =
+ typeof window !== 'undefined' &&
+  typeof window.document !== 'undefined' &&
+  typeof window.document.createElement !== 'undefined'
+
+/**
+ * Custom hook for reading
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useGetSet (task/8)

```diff
-const useGetSet = initialState => {
+const useGetSet = initialState => {
+
+  const [state, setState] = useState(initialState);
+
+  return [state, setState];
+};
+
+export default useGetSet;
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useInterval (task/9)

```diff
-const useInterval = (callback, delay) => {
+const useInterval = (callback, delay) => {
+
+    const savedCallback = useRef();
+
+    // Remember the latest callback.
+    useEffect(() => {
+        savedCallback.current = callback;
+    }, [callback]);
+
+    // Set up the interval.
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <View
+      style={{
+        alignItems: 'center',
+        justifyContent: 'center',
+        backgroundColor: 'rgba(0,0,0,0.8)',
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div className="loader">
+      <style jsx>{`
+        .loader {
+          margin: 0 auto;
+          width: ${size}px;
+          height: ${size
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div className="loader-container">
+      <svg
+        className="loader"
+        width={size}
+        height={size}
+        viewBox="0 0 100 100"
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div className={`w-6 h-6 border-2 border-white flex items-center justify-center bg-white ${size}`}>
+      <div className="animate
```

#### Loader (task/10)

```diff
-const Loader = ({ size }) => {
+const Loader = ({ size }) => {
+
+  return (
+    <div className={`loader ${size}`}>
+      <div className="spinner">
+        <div className="bounce1" />
+        <div className="b
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const close = (e) => {
+    if (e.target.className === 'modal') {
+      onClose();
+    }
+  };
+
+  return (
+    <div className={`
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const classes = useStyles();
+  return (
+    <Dialog open={isVisible}>
+      <DialogTitle>{title}</DialogTitle>
+      <DialogContent>{content}</DialogContent
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const closeModal = () => {
+    onClose && onClose();
+  };
+
+  return (
+    <ModalWrapper
+      style={{
+        display: isVisible ? "flex" :
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const handleClose = useCallback(() => {
+    onClose()
+  }, [onClose])
+
+  return (
+    <ModalBlock
+      isVisible={isVisible}
+      onClose={
```

#### Modal (task/11)

```diff
-const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
+
+  const handleClose = () => {
+    onClose();
+  };
+
+  return (
+    <ModalWrapper isVisible={isVisible}>
+      <ModalOverlay />
+      <Mod
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+    const [entry, setEntry] = useState({});
+    const [intersectionRatio, setIntersectionRatio] = useState(0);
+    const [isIntersecting, setIsIntersecting
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [intersection, setIntersection] = useState(null);
+  const observer = useRef(null);
+
+  useEffect(() => {
+    if (ref.current) {
+      observer.current
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [entry, setEntry] = useState(null);
+  const [isIntersecting, setIsIntersecting] = useState(false);
+
+  useEffect(() => {
+    const observer =
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const [isIntersecting, setIsIntersecting] = useState(false);
+
+  useEffect(() => {
+    const observer = new IntersectionObserver(entries => {
+      entries.for
```

#### useIntersectionObserver (task/12)

```diff
-const useIntersectionObserver = (ref, options) => {
+const useIntersectionObserver = (ref, options) => {
+
+  const callback = useCallback(
+    (entries) => {
+      entries.forEach((entry) => {
+        if (entry.isIntersecting) {
+          options.onIntersecting()
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+name, label, value, onChange, min, max, step, id, error }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+style, ...props }) => {
+  const styles = {
+    ...style,
+    width: '100%',
+    height: '100%',
+    position: 'absolute',
+    top: 0,
+   
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+label, onChange, value, options, type, className, ...rest }) => {
+  const [currentValue, setCurrentValue] = useState(value);
+  const [left, setLeft] = useState(value
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+name, label, value, onChange, min, max, step }) => {
+  return (
+    <div className="slider">
+      <div className="form-group">
+        <label htmlFor={name
```

#### Slider (task/13)

```diff
-const Slider = ({ 
+const Slider = ({ 
+children, ...props }) => {
+  return (
+    <div className={cx(styles.wrapper, 'slider')}>
+      <ReactSlick {...props}>{children}</Re
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+  const [isVisible, setIsVisible] = useState(initialState);
+
+  const toggle = () => setIsVisible(!isVisible);
+
+  return { isVisible, toggle };
+};
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+	const [state, setState] = useState(initialState);
+
+	const toggle = useCallback(() => {
+		setState(s => !s);
+	}, []);
+
+	return [state,
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+	const [state, setState] = useState(initialState);
+
+	const toggle = () => setState(!state);
+
+	return [state, toggle];
+};
+
+export default useToggler;
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+	const [state, setState] = useState(initialState);
+
+	const setTrue = () => setState(true);
+	const setFalse = () => setState(false);
+
+	return [state, set
```

#### useToggler (task/14)

```diff
-const useToggler = initialState => {
+const useToggler = initialState => {
+
+  const [toggler, setToggler] = useState(initialState);
+
+  const toggle = () => {
+    setToggler(!toggler);
+  };
+
+  return [togg
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [value, setValue] = useState(false);
+  const onMouseOver = () => setValue(true);
+  const onMouseOut = () => setValue(false);
+  return {
+   
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [state, setState] = useState({
+    isHovering: false,
+  });
+
+  const [hovered, setHovered] = useState(false);
+
+  const handleHover =
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+    const [hover, setHover] = useState(false);
+    const onMouseEnter = () => setHover(true);
+    const onMouseLeave = () => setHover(false);
+    return
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+    const [hover, setHover] = useState(false);
+    const toggleHover = useCallback(() => setHover(!hover), [hover]);
+    return { hover, toggleHover };
```

#### useHover (task/15)

```diff
-const useHover = () => {
+const useHover = () => {
+
+  const [hovered, setHovered] = useState(false);
+
+  const handleHover = () => {
+    setHovered(!hovered);
+  };
+
+  return { hovered, handleH
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+export default usePrevious;
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+const useDate = (date) => {
+ 
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+export default usePrevious;
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+  const ref = useRef();
+  useEffect(() => {
+    ref.current = value;
+  });
+  return ref.current;
+};
+
+export default usePrevious;
```

#### usePrevious (task/16)

```diff
-const usePrevious = value => {
+const usePrevious = value => {
+
+    const ref = useRef();
+    useEffect(() => {
+        ref.current = value;
+    });
+    return ref.current;
+};
+
+export default usePrevious;
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  const matches = useMedia(query);
+  return matches ? whenTrue : whenFalse;
+};
+
+const Container = styled.div`
+  position: relative;
+  width: 100%;
+  height: 100
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  return useContext(MediaQueryContext) === query ? whenTrue : whenFalse;
+};
+
+const useKeyHandler = (callback, key, action) => {
+  useEffect(() => {
+    const handler
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  const breakpoint = window.matchMedia(query);
+  return breakpoint.matches ? whenTrue : whenFalse;
+};
+
+const ResponsiveMenu = ({ className, ...props }) => {
+ 
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  const mediaQuery = window.matchMedia(query);
+  const [matches, setMatches] = useState(mediaQuery.matches);
+
+  useEffect(() => {
+    const handler = event =>
```

#### useMediaQuery (task/17)

```diff
-const useMediaQuery = (query, whenTrue, whenFalse) => {
+const useMediaQuery = (query, whenTrue, whenFalse) => {
+
+  const mql = window.matchMedia(query);
+  return mql.matches ? whenTrue : whenFalse;
+};
+
+const useWidth = () => {
+  const isLg = useMediaQuery
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+    return initialState === undefined ? defaultState : initialState;
+};
+
+const useMappedState = (state, mapFn) => {
+    return mapFn(state);
+};
+
+const useMap
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+  if (initialState === undefined) {
+    return defaultState;
+  }
+
+  return initialState;
+};
+
+export default useDefault;
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+  if (initialState === undefined) {
+    return defaultState;
+  }
+
+  return initialState;
+};
+
+export const useList = (state = [], { type, payload } = {}) => {
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+    if (initialState === undefined) {
+        return defaultState;
+    }
+    return initialState;
+};
+
+export default useDefault;
```

#### useDefault (task/18)

```diff
-const useDefault = (defaultState, initialState) => {
+const useDefault = (defaultState, initialState) => {
+
+  if (typeof initialState === 'undefined') {
+    return defaultState;
+  }
+  return initialState;
+};
+
+const useLocalStorage = (key, initialState) => {
+  const
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [tag, setTag] = useState('');
+  const [tagList, setTagList] = useState(tags);
+
+  const handleAddTag = (e) => {
+    e.pre
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [input, setInput] = useState('');
+  const [newTag, setNewTag] = useState([]);
+
+  const addTag = (tag) => {
+    setNewTag((
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [currentTag, setCurrentTag] = useState('');
+  const [tagsList, setTagsList] = useState(tags);
+
+  const addTag = (e) => {
+    e.
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [input, setInput] = useState('');
+  const [selected, setSelected] = useState([]);
+
+  const onChange = (e) => {
+    setInput(e.
```

#### TagInput (task/19)

```diff
-const TagInput = ({ tags }) => {
+const TagInput = ({ tags }) => {
+
+  const [newTag, setNewTag] = useState('');
+  const [editing, setEditing] = useState(false);
+  const [inputRef, setInputRef] = useState(
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const classes = useStyles();
+  const [checked, setChecked] = useState([]);
+
+  const handleToggle = value => () => {
+    const currentIndex = checked.indexOf(value
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const { state, dispatch } = useOvermind();
+
+  const checked = state.selectedItems;
+
+  const handleChange = (event) => {
+    const { target } = event;
+    const selected = state
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const [selected, setSelected] = useState([]);
+
+  const onSelect = (selectedValue) => {
+    if (selected.includes(selectedValue)) {
+      setSelected(selected.filter
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+  const [selectedOptions, setSelectedOptions] = useState([]);
+
+  const onSelect = option => {
+    const index = selectedOptions.indexOf(option);
+    if (index >= 0) {
```

#### MultiselectCheckbox (task/20)

```diff
-const MultiselectCheckbox = ({ options, onChange }) => {
+const MultiselectCheckbox = ({ options, onChange }) => {
+
+    const [state, setState] = useState({});
+
+    const toggle = (key) => {
+        setState({
+            ...state,
+            [key]: !state[key]
+        });
+   
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const buildData = (data, count = 0) => {
+    if (data) {
+      return data.map((item, i) => {
+        const list = buildData(item.children, count +
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  return (
+    <>
+      {isOrdered ? (
+        <ol>
+          {data.map((item, i) => (
+            <li key={i}>{item}</li>
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const renderData = () => {
+    if (isOrdered) {
+      return data.map((item, i) => (
+        <OrderedItem key={i} data={item} />
+      ));
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const [isOpen, setIsOpen] = useState(true);
+  const [isOrderedByDate, setIsOrderedByDate] = useState(isOrdered);
+
+  return (
+    <
```

#### DataList (task/21)

```diff
-const DataList = ({ isOrdered = false, data }) => {
+const DataList = ({ isOrdered = false, data }) => {
+
+  const ordered = isOrdered ? 'ol' : 'ul';
+  return (
+    <>
+      <StyledHeader>
+        <span>Data</span>
+      </StyledHeader>
+     
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const [index, setIndex] = useState(0);
+  const [translateValue, setTranslateValue] = useState(0);
+  const { width } = useWindowDimensions();
+
+  const
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const [slideIndex, setSlideIndex] = useState(0);
+  const { isMobile } = useMobile();
+
+  const onClickLeft = () => {
+    if (slideIndex > 0
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const isSlide = carouselItems.length > 1;
+  const [currentSlide, setCurrentSlide] = useState(0);
+  const [currentDirection, setCurrentDirection] = use
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const {
+    carousel,
+    carouselImage,
+    carouselContent,
+    carouselTitle,
+    carouselContentContainer,
+    carouselContainer,
+    carouselButton,
+    car
```

#### Carousel (task/22)

```diff
-const Carousel = ({ carouselItems, ...rest }) => {
+const Carousel = ({ carouselItems, ...rest }) => {
+
+  const [active, setActive] = useState(0);
+  const [interval, setInterval] = useState(0);
+  const [direction, setDirection] = useState(false);
+
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+
+  const update = (updater) => {
+    const newState = Object.assign({}, state, updater);
+    setState
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+  const setMergeState = (obj = {}) => {
+    setState({ ...state, ...obj });
+  };
+  return [
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+
+  return [
+    state,
+    (newState) => {
+      setState((prevState) => {
+        const updatedState = {
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+
+  return [
+    state,
+    useCallback(
+      (newState) => {
+        setState({
+          ...state,
+         
```

#### useMergeState (task/23)

```diff
-const useMergeState = (initialState = {}) => {
+const useMergeState = (initialState = {}) => {
+
+  const [state, setState] = useState(initialState);
+
+  const mergeState = (newState) => {
+    setState((oldState) => ({ ...oldState, ...newState }));
+ 
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [loading, setLoading] = useState(false);
+  const [value, setValue] = useState(undefined);
+  const [error, setError] = useState(undefined);
+
+ 
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const hook = useCallback(async () => {
+    const task = fn();
+    if (task) {
+      hook.loading = true;
+      await task;
+      hook.loading = false;
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [loading, setLoading] = useState(false);
+  const [error, setError] = useState(null);
+  const [result, setResult] = useState(null);
+
+  useEffect
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [isLoading, setIsLoading] = useState(false);
+  const [error, setError] = useState(null);
+  const [isLoaded, setIsLoaded] = useState(
```

#### useAsync (task/24)

```diff
-const useAsync = fn => {
+const useAsync = fn => {
+
+  const [loading, setLoading] = useState(false);
+  const [error, setError] = useState(null);
+  const [result, setResult] = useState(null);
+
+  const handle
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  const lockBodyScroll = useCallback(() => {
+    const currentTarget = event.currentTarget;
+    const { body } = document;
+    const { activeElement } = document;
+    if (activeElement
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  const [isScrollFreeze, setIsScrollFreeze] = useState(false);
+
+  useEffect(() => {
+    window.addEventListener('scroll', handleScroll);
+    return () => {
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  const [state, setState] = useState(false);
+  const handleScroll = () => {
+    if (
+      window.scrollY === 0 ||
+      document.documentElement.scrollTop === 0 ||
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+    const originalStyle = window.getComputedStyle(document.body).overflow;
+    document.body.style.overflow = 'hidden';
+    return () => {
+        document.body.style.over
```

#### useBodyScrollLock (task/25)

```diff
-const useBodyScrollLock = () => {
+const useBodyScrollLock = () => {
+
+  const [isBodyOverflowHidden, setIsBodyOverflowHidden] = useState(false);
+
+  const hideBodyOverflow = () => {
+    if (!isBodyOverflowHidden) {
+      setIs
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleChange = e => {
+    setValues({
+      ...values,
+      [e.target.name]: e.target.value
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+    const [values, setValues] = useState(initialValues);
+
+    const onChange = e => {
+        setValues({
+            ...values,
+            [e.target.name]: e.target.value
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleChange = event => {
+    setValues({
+      ...values,
+      [event.target.name]: event.target.value
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+  const [values, setValues] = useState(initialValues);
+
+  const handleChange = e => {
+    setValues({
+      ...values,
+      [e.target.name]: e.target.value
```

#### useForm (task/26)

```diff
-const useForm = initialValues => {
+const useForm = initialValues => {
+
+    const [values, setValues] = useState(initialValues);
+
+    const handleInputChange = event => {
+        event.persist();
+        setValues(values => ({
+            ...values,
+            [
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  const hasPortal = el.closest('.portal')
+  const portal = hasPortal ? hasPortal : document.createElement('div')
+  portal.classList.add('portal')
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  const documentFragment = document.createDocumentFragment();
+  const container = document.createElement('div');
+  const root = document.createElement('div');
+  root.classList.add('portal
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  if (!el) return null;
+  const elRef = useRef(null);
+  useEffect(() => {
+    const node = elRef.current;
+    if (node && el) {
+     
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  if (!el) return;
+  if (el.hasAttribute('data-portal')) return;
+  el.setAttribute('data-portal', 'true');
+  if (document.body.cont
```

#### usePortal (task/27)

```diff
-const usePortal = el => {
+const usePortal = el => {
+
+  if (!el) return;
+  if (el.nodeType === 1) {
+    el.removeAttribute('aria-hidden');
+    el.setAttribute('aria-modal', true);
+    el.
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  return (
+    <a
+      href={`mailto:${email}?subject=${subject}&body=${body}`}
+      className="text-blue-400 hover:text-blue-
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  return (
+    <a
+      href={`mailto:${email}?subject=${subject}&body=${body}`}
+      rel="noopener noreferrer"
+      target="
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  const subjectAttr = (subject) ? `subject=${subject}` : '';
+  const bodyAttr = (body) ? `body=${body}` : '';
+  const mailtoString =
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  return (
+    <a
+      href={`mailto:${email}?subject=${subject}&body=${body}`}
+      target="_blank"
+      rel="noopener nore
```

#### Mailto (task/28)

```diff
-const Mailto = ({ email, subject = '', body = '', children }) => {
+const Mailto = ({ email, subject = '', body = '', children }) => {
+
+  const subjectValue = subject.trim()
+  const bodyValue = body.trim()
+
+  const handleMailto = () => {
+    if (subjectValue) {
+      window.location.href = `
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const isPressed = React.useRef(false);
+
+  const onKeyPress = React.useCallback(
+    e => {
+      if (e.key === targetKey) {
+        isPressed.
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+	const [keyPressed, setKeyPressed] = useState(false);
+
+	const onKeyDown = (event) => {
+		if (event.key === targetKey) {
+			set
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const [keyPressed, setKeyPressed] = useState(false);
+
+  const keyPress = ({ key }) => {
+    if (key === targetKey) {
+      setKeyPressed(true);
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const pressHandlers = useCallback(() => {
+    console.log(`Key pressed ${targetKey}`);
+  }, [targetKey]);
+
+  const upHandlers = useCallback(() => {
```

#### useKeyPress (task/29)

```diff
-const useKeyPress = targetKey => {
+const useKeyPress = targetKey => {
+
+  const [keyPressed, setKeyPressed] = useState(false);
+
+  const keyDownHandler = ({ key }) => {
+    if (key === targetKey) {
+      setKeyPressed(true
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const [timeLeft, setTimeLeft] = useState(0);
+
+  useEffect(() => {
+    const interval = setInterval(() => {
+      setTimeLeft(initialTime => initialTime -
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const time = {
+    hours,
+    minutes,
+    seconds,
+  };
+
+  return (
+    <>
+      <Row className="justify-content-center">
+        <Col>
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const formattedTime = `${formatNumber(hours)}:${formatNumber(minutes)}:${formatNumber(seconds)}`;
+  return (
+    <div className="countdown">
+      <span class
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const [time, setTime] = useState({ hours, minutes, seconds });
+  const getTimeUntil = () => {
+    const { hours, minutes, seconds } = time;
+    const timeRemaining =
```

#### CountDown (task/30)

```diff
-const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
+
+  const [timer, setTimer] = useState(0);
+  const [isCounting, setIsCounting] = useState(false);
+
+  useEffect(() => {
+    if (isCounting
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [show, setShow] = useState(isDefaultShown);
+  const onMouseEnter = () => setShow(true);
+  const onMouseLeave = () => setShow(false);
+
+  use
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [isShown, setIsShown] = useState(isDefaultShown);
+  const [isTimeoutShown, setIsTimeoutShown] = useState(false);
+
+  useEffect(()
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [isVisible, setIsVisible] = useState(isDefaultShown);
+  const [timeLeft, setTimeLeft] = useState(timeout);
+
+  useEffect(() => {
+   
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [state, setState] = useState({
+    show: isDefaultShown,
+    timeout: timeout,
+    type: type,
+    message: message,
+  });
+
+  useEffect(()
```

#### Alert (task/31)

```diff
-const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
+
+  const [isShown, setIsShown] = useState(isDefaultShown);
+  const toggleIsShown = () => setIsShown(!isShown);
+
+  useEffect(() =>
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [hash, setHash] = useState(window.location.hash.substr(1));
+
+  useEffect(() => {
+    const handler = () => setHash(window.location.hash.sub
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [hash, setHash] = useState('');
+
+  useEffect(() => {
+    const { pathname, hash } = window.location;
+    const uri = `${pathname}${
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [hash, setHash] = useState<string | null>(null);
+
+  useEffect(() => {
+    setHash(window.location.hash);
+    window.addEventListener('hashchange',
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const [hash, setHash] = useState('');
+  const [page, setPage] = useState(1);
+  const [isNextPage, setIsNextPage] = useState(true);
```

#### useHash (task/32)

```diff
-const useHash = () => {
+const useHash = () => {
+
+  const history = useHistory();
+  const hash = useLocation().hash;
+  const hashMatch = hash.match(/^#\/?(.+)/);
+  const hashLink = hashMatch ? hashMatch
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [state, setState] = useState(initialState);
+  const [show, setShow] = useState(condition);
+
+  const action = useCallback(() => {
+    setShow(true);
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [state, setState] = useState(initialState);
+  useEffect(() => {
+    const timeout = setTimeout(() => {
+      if (condition) {
+        setState(!state
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [value, setValue] = useState(initialState);
+  const [delayedValue, setDelayedValue] = useState(initialState);
+
+  useEffect(() => {
+    const timeout =
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [state, setState] = useState(initialState);
+  const isReady = useRef(false);
+
+  useEffect(() => {
+    if (!isReady.current && condition) {
+     
```

#### useDelayedState (task/33)

```diff
-const useDelayedState = (initialState, condition) => {
+const useDelayedState = (initialState, condition) => {
+
+  const [state, setState] = useState(initialState);
+  const [delayedState, setDelayedState] = useState(initialState);
+
+  useEffect(() => {
+    const timer =
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+  const [searchParams, setSearchParams] = useState([]);
+  const [searchParam, setSearchParam] = useState(param);
+
+  useEffect(() => {
+    const { search
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+    const {
+        location: { search },
+    } = window;
+    const params = new URLSearchParams(search);
+    return params.get(param);
+};
+
+const useParams =
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+    return useMemo(() => queryString.parse(param), [param]);
+};
+
+const useSearchParamValue = param => {
+    const parsed = useSearchParam(param);
+    return useMemo
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+  const url = window.location.href;
+  const searchParam = url.split("?")[1];
+  if (searchParam) {
+    const params = searchParam.split("&");
+    const result
```

#### useSearchParam (task/34)

```diff
-const useSearchParam = param => {
+const useSearchParam = param => {
+
+  const { location } = useReactRouter();
+  const searchParams = new URLSearchParams(location.search);
+  return searchParams.get(param);
+};
+
+const useQuery
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [update, setUpdate] = useState(false);
+  const forceUpdate = useCallback(() => setUpdate(v => !v), []);
+  return [update, forceUpdate];
+};
+
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [createData, setCreateData] = useState(init.create);
+  const [updateData, setUpdateData] = useState(init.update);
+  const [deleteData, setDeleteData]
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [update, { loading }] = useMutation(UPDATE_DEVICE, {
+    refetchQueries: [{ query: GET_DEVICES }],
+    awaitRefetchQueries: true,
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [updating, setUpdating] = useState(false);
+  const set = useCallback(
+    (update: string) => {
+      setUpdating(true);
+      window.fetch(
```

#### useUpdate (task/35)

```diff
-const useUpdate = () => {
+const useUpdate = () => {
+
+  const [state, setState] = useState<ISetState>({
+    id: '',
+    content: '',
+    isUpdate: false,
+  });
+
+  const onChange = (e:
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const handleChange = (value) => {
+    onValueChange(value);
+  };
+
+  return (
+    <SelectBase
+      {...rest}
+      name={rest.name}
+      value={
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const handleChange = value => {
+    onValueChange(value);
+  };
+
+  return (
+    <SelectComp
+      {...rest}
+      values={values}
+      onChange={handleChange}
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const [valuesArray, setValuesArray] = useState([]);
+
+  useEffect(() => {
+    if (Array.isArray(values)) {
+      setValuesArray(values);
+    }
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const classes = useStyles()
+  const theme = useTheme()
+  const [open, setOpen] = useState(false)
+
+  const openMenu = () => {
+    setOpen(true)
```

#### Select (task/36)

```diff
-const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
+
+  const [isOpen, setIsOpen] = useState(false);
+  const ref = useRef();
+
+  const handleToggle = () => {
+    setIsOpen(!isOpen);
+  };
+
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [errors, setErrors] = useState([]);
+  const ref = useRef();
+
+  const onChange = (e) => {
+    const newValue = e.target.value;
+   
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [warning, setWarning] = useState(false);
+  const [text, setText] = useState(value);
+
+  const handleChange = (e) => {
+    const { value } = e
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  return (
+    <TextareaAutosize
+      value={value}
+      onChange={e => {
+        if (e.target.value.length > limit) {
+          e.target.value =
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  const [text, setText] = useState(value);
+  const [isOver, setIsOver] = useState(false);
+
+  const handleChange = (e) => {
+    setText(e
```

#### LimitedWordTextarea (task/37)

```diff
-const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
+
+  return (
+    <Fragment>
+      <ReactQuill
+        value={value}
+        readOnly
+        modules={{
+          toolbar: false,
+        }}
+        style={{
+          width
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+	const [scrollTop, setScrollTop] = useState(0);
+
+	useEffect(() => {
+		const onScroll = () => {
+			const scrollHeight = document.documentElement.scroll
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  useEffect(() => {
+    const handleScroll = () => {
+      const inner = window.innerHeight;
+      const height = document.documentElement.scrollHeight;
+      const scrolled = (window.
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  useEffect(() => {
+    const handleScroll = () => {
+      callback();
+    };
+    window.addEventListener('scroll', handleScroll);
+    return () => {
+      window.removeEvent
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  useEffect(() => {
+    const handleScroll = () => {
+      callback();
+    };
+    window.addEventListener('scroll', handleScroll);
+    return () => {
+      window.removeEvent
```

#### useOnWindowScroll (task/38)

```diff
-const useOnWindowScroll = callback => {
+const useOnWindowScroll = callback => {
+
+  const handleScroll = () => {
+    const { scrollY } = window;
+    const isScrolledToBottom = scrollY >= window.innerHeight;
+    const isAtTop = scrollY === 0;
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+  const handleClick = (e) => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() =>
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    const handleClick = e => {
+        if (ref.current && !ref.current.contains(e.target)) {
+            callback();
+        }
+    };
+
+    useEffect(() => {
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+  const handleClick = (e) => {
+    if (ref.current && !ref.current.contains(e.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() =>
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+  const handleClick = event => {
+    if (ref.current && !ref.current.contains(event.target)) {
+      callback();
+    }
+  };
+
+  useEffect(() => {
```

#### useClickInside (task/39)

```diff
-const useClickInside = (ref, callback) => {
+const useClickInside = (ref, callback) => {
+
+    const handleClick = (e) => {
+        if (ref.current && !ref.current.contains(e.target)) {
+            callback()
+        }
+    }
+
+    useEffect(() =>
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+const USE_DOM = isDOMavailable && IS_BROWSER;
+
+const shared
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+/**
+ * DESIGN NOTES
+ *
+ * The following is a description of the algorithm
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+typeof window !== 'undefined' && window.document && window.document.createElement);
+
+const ReactDOMServer = {
+  renderToString: (element: React.ReactElement<any>) => {
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+
+  typeof window !== 'undefined' &&
+  window.document &&
+  window.document.createElement
+);
+
+const dom = {
+  isReal: isDOMavailable,
+  isTest: false
```

#### useSSR (task/40)

```diff
-const isDOMavailable = !!(
+const isDOMavailable = !!(
+typeof window !== 'undefined' && window.document && window.document.createElement);
+
+module.exports = isDOMavailable;
+
+},{}],21:[function(require,module,exports){
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const rowsArray = new Array(rows).fill('');
+  const rowsString = rowsArray.join('\n');
+  const text = `${rowsString}${value}`;
+  const [line
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const limitedValue = value.length > limit ? `${value.substring(0, limit)}...` : value;
+  return (
+    <textarea
+      className="limited-textarea"
+     
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [count, setCount] = useState(value.length);
+  const [valueSaved, setValueSaved] = useState(value);
+
+  const handleChange = e => {
+    const text
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [isEmpty, setIsEmpty] = useState(true);
+  const [isOverflow, setIsOverflow] = useState(false);
+  const [isEmptyLimit, setIsEmptyLimit]
```

#### LimitedTextarea (task/41)

```diff
-const LimitedTextarea = ({ rows, cols, value, limit }) => {
+const LimitedTextarea = ({ rows, cols, value, limit }) => {
+
+  const [text, setText] = useState(value);
+  const [truncated, setTruncated] = useState(false);
+
+  const onChange = (e) => {
+    setText
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  const mounted = useRef(false);
+
+  useEffect(() => {
+    if (!mounted.current) {
+      mounted.current = true;
+    } else {
+      onMountHandler();
+    }
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  return (WrappedComponent) => {
+    return (props) => {
+      useEffect(() => {
+        onMountHandler(props);
+      }, []);
+      return <WrappedComponent {
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  const useOnMount = () => {
+    useEffect(() => {
+      onMountHandler();
+    }, []);
+  };
+
+  return useOnMount;
+};
+
+export default useComponentDidMount
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  useEffect(() => {
+    if (onMountHandler) {
+      onMountHandler();
+    }
+  }, []);
+};
+
+export default useComponentDidMount;
```

#### useComponentDidMount (task/42)

```diff
-const useComponentDidMount = onMountHandler => {
+const useComponentDidMount = onMountHandler => {
+
+  useEffect(() => {
+    onMountHandler()
+  }, [])
+}
+
+export default useComponentDidMount
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const { acceptedFiles, getRootProps, getInputProps } = useDropzone({
+    onDrop,
+    accept: "image/*",
+  });
+
+  return (
+    <div {...get
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const drop = useRef(null);
+
+  const handleDrop = (e) => {
+    e.preventDefault();
+    e.stopPropagation();
+    onDrop(e.dataTransfer.files
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const onDropHandler = useCallback(
+    acceptedFiles => {
+      const file = acceptedFiles[0];
+      const reader = new FileReader();
+      reader.onabort = () => console.log('
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const fileRef = useRef(null);
+
+  const onDragOver = (e) => {
+    e.preventDefault();
+  };
+
+  const onDropFile = (e) => {
+    e
```

#### FileDrop (task/43)

```diff
-const FileDrop = ({ onDrop }) => {
+const FileDrop = ({ onDrop }) => {
+
+  const classes = useStyles();
+  const [file, setFile] = useState();
+  const [dragOver, setDragOver] = useState(false);
+
+  const handleDrop = (e)
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ data, labelKey, onClick }) => {
+  const [{ isDragging }, drag] = useDrag({
+    item: { type: ItemTypes.CARD, data },
+    end: (item, monitor) =>
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+
+  tree,
+  onNodeChange,
+  onNodeDelete,
+  onNodeCreate,
+  onNodeUp,
+  onNodeDown,
+  onNodeEdit,
+  onNodeDragStart,
+  on
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ treeData, setTreeData, folder, setFolder }) => {
+  const { path, name } = folder;
+  const [isExpanded, setIsExpanded] = useState(false);
+  const [isRen
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+ id, children, className, onChange, data, field, value, onToggle, onExpand }) => {
+  const [state, setState] = useState({ expandedKeys: [], selectedKeys: [] });
```

#### TreeView (task/44)

```diff
-const TreeView = ({
+const TreeView = ({
+
+  classes,
+  className,
+  children,
+  ...rest
+}: TreeViewProps): ReactElement => {
+  const cls = clsx(classes.root, className);
+  return (
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    const persistState = JSON.parse(localStorage.getItem(name));
+    return persistState !== null ? persistState : defaultValue;
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    const persistedState = localStorage.getItem(name);
+    return persistedState !== null ? JSON.parse(persistedState) : default
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [value, setValue] = useState(
+    JSON.parse(window.localStorage.getItem(name)) || defaultValue
+  );
+
+  const setValueToLocalStorage = useCallback(() =>
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    try {
+      const storageValue = localStorage.getItem(name);
+      if (storageValue) {
+        return JSON.parse(
```

#### usePersistedState (task/45)

```diff
-const usePersistedState = (name, defaultValue) => {
+const usePersistedState = (name, defaultValue) => {
+
+  const [state, setState] = useState(() => {
+    try {
+      const serializedState = localStorage.getItem(name);
+      if (serializedState === null) {
+        return
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [windowSize, setWindowSize] = useState({
+    width: undefined,
+    height: undefined,
+  });
+
+  useEffect(() => {
+    function handleResize() {
+      set
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [size, setSize] = useState(window.innerWidth);
+
+  useEffect(() => {
+    const handleResize = () => {
+      setSize(window.innerWidth);
+    };
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [windowSize, setWindowSize] = useState({
+    width: undefined,
+    height: undefined,
+  });
+
+  useEffect(() => {
+    function handleResize() {
+      set
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [size, setSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffect(() => {
+    const handleResize =
```

#### useWindowSize (task/46)

```diff
-const useWindowSize = () => {
+const useWindowSize = () => {
+
+  const [size, setSize] = useState({
+    width: window.innerWidth,
+    height: window.innerHeight,
+  });
+
+  useEffect(() => {
+    const onResize =
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const onChange = useCallback(
+    (e) => {
+      onValueChange(e.target.value);
+    },
+    [onValueChange]
+  );
+
+  return <input value={value
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const handleChange = e => {
+    onValueChange(e.target.value);
+  };
+
+  return <input value={value} onChange={handleChange} {...rest} />;
+};
+
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const [internalValue, setInternalValue] = useState(value);
+
+  useEffect(() => {
+    setInternalValue(value);
+  }, [value]);
+
+  const onChange = event => {
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const onChange = event => {
+    const { target: { value } } = event;
+    onValueChange(value);
+  };
+
+  return (
+    <input value={value} onChange={on
```

#### ControlledInput (task/47)

```diff
-const ControlledInput = ({ value, onValueChange, ...rest }) => {
+const ControlledInput = ({ value, onValueChange, ...rest }) => {
+
+  const [isFocused, setIsFocused] = useState(false);
+  const onBlur = () => setIsFocused(false);
+  const onFocus = () => setIsFocused(true
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  const [sorted, setSorted] = useState([])
+  const [searchQuery, setSearchQuery] = useState('')
+  const [checked, setChecked] = useState([])
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  const classes = useStyles();
+  const [page, setPage] = useState(0);
+  const [rowsPerPage, setRowsPerPage] = useState(5);
+
+  const handleChange
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  const columns = React.useMemo(
+    () => [
+      {
+        Header: 'Name',
+        accessor: 'name',
+      },
+      {
+        Header: 'Age',
+       
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  return (
+    <div className="data-table">
+      <table>
+        <thead>
+          <tr>
+            <th>name</th>
+            <th>price</th>
```

#### DataTable (task/48)

```diff
-const DataTable = ({ data }) => {
+const DataTable = ({ data }) => {
+
+  const columns = React.useMemo(
+    () => [
+      {
+        Header: 'Date',
+        accessor: 'date',
+      },
+      {
+        Header: 'Stock',
+       
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const componentWillUnmount = componentProps => {
+    // componentWillUnmount is called when unmounting. However, we have already ran componentWillUnmount
+    // from componentWillUnmount. So we can
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const ref = useRef(null);
+  useEffect(() => {
+    ref.current = onUnmountHandler;
+    return () => {
+      ref.current();
+    };
+  }, []);
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  return useEffect(() => {
+    return () => {
+      onUnmountHandler();
+    };
+  }, []);
+};
+
+export default useComponentWillUnmount;
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  const {
+    current: { onUnmount = () => {} }
+  } = React.useRef(onUnmountHandler);
+
+  React.useEffect(() => {
+    return () => {
+     
```

#### useComponentWillUnmount (task/49)

```diff
-const useComponentWillUnmount = onUnmountHandler => {
+const useComponentWillUnmount = onUnmountHandler => {
+
+  useEffect(() => {
+    return () => {
+      onUnmountHandler()
+    }
+  }, [])
+}
+
+export default useComponentWillUnmount
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [activeIndex, setActiveIndex] = useState(defaultIndex);
+
+  const _onTabClick = index => {
+    setActiveIndex(index);
+    onTabClick && onTabClick(index);
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [currentIndex, setCurrentIndex] = useState(defaultIndex);
+
+  const getTabItems = () => {
+    return React.Children.map(children, (child, index) => {
+      return
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [activeIndex, setActiveIndex] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setActiveIndex(index);
+    onTabClick && onTabClick(index);
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [active, setActive] = useState(defaultIndex);
+
+  const onClick = index => {
+    setActive(index);
+    onTabClick(index);
+  };
+
+  return (
+   
```

#### Tabs (task/50)

```diff
-const TabItem = props => <div {...props} />;
-
-const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+const TabItem = props => <div {...props} />;
+
+const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
+
+  const [current, setCurrent] = useState(defaultIndex);
+
+  const handleTabClick = index => {
+    setCurrent(index);
+    onTabClick && onTabClick(index);
+  };
+
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return (dispatch: any) => {
+    dispatch(getOnLineStatusRequest());
+    // eslint-disable-next-line
+    setTimeout(() => {
+      dispatch(getOnLineStatus
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return async (dispatch: ThunkDispatch<{}, {}, any>) => {
+    const localInfo = await wx.getSystemInfo();
+    const status = localInfo.networkType === 'none' ?
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  let onLine = false;
+  try {
+    if (typeof window !== 'undefined') {
+      onLine = navigator.onLine;
+    }
+  } catch (e) {
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  let onlineStatus = document.body.getAttribute('online-status');
+  if (onlineStatus === 'on') {
+    return true;
+  }
+  return false;
+};
+
+export default function Online
```

#### useNavigatorOnLine (task/51)

```diff
-const getOnLineStatus = () =>
+const getOnLineStatus = () =>
+ {
+  return true;
+};
+
+export const getData = (params: any) => {
+  return new Promise((resolve, reject) => {
+    setTimeout(() => {
+      const list = JSON.
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [showPassword, setShowPassword] = useState(false);
+
+  const handleClick = () => {
+    setShowPassword(!showPassword);
+  };
+
+  return (
+    <div>
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [show, setShow] = useState(false);
+
+  return (
+    <div className="password-revealer">
+      <input
+        type={show ? "text" : "password"}
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [reveal, setReveal] = useState(false);
+
+  return (
+    <div>
+      <TextField
+        id="standard-password-input"
+        type={reveal ?
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+  const [showPassword, setShowPassword] = useState(false);
+
+  const handleClick = (e) => {
+    e.preventDefault();
+    setShowPassword(!showPassword);
+  };
```

#### PasswordRevealer (task/52)

```diff
-const PasswordRevealer = ({ value }) => {
+const PasswordRevealer = ({ value }) => {
+
+    const [show, setShow] = useState(false);
+    const onClick = () => setShow(!show);
+
+    return (
+        <div className="password-revealer">
+            <div
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const className = `react-star-rating__star ${marked ? 'react-star-rating__star--active' : ''}`;
+  return (
+    <svg className={className} xml
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const colors = ['#ffaf61', '#ffd08b', '#ffffbf', '#d9ef8b', '#a6d96a'];
+  const backgroundColor = colors[star
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const classNames = marked ? 'star marked' : 'star';
+  return <div className={classNames}>{starId}</div>;
+};
+
+export default Star;
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const { onMarked, onUnmarked } = useMarkedCallback(starId);
+  const isMarked = marked;
+
+  return (
+    <div className="star" onClick={isMarked
```

#### StarRating (task/53)

```diff
-const Star = ({ marked, starId }) => {
+const Star = ({ marked, starId }) => {
+
+  const starStyle = {
+    backgroundColor: marked ? "#4ca984" : "#fff",
+    border: marked ? "1px solid transparent" : "1px solid #c1c1c1",
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const didUpdate = useCallback(() => {
+    callback();
+  }, [callback]);
+
+  if (condition) {
+    useEffect(didUpdate, [condition]);
+  }
+};
+
+export default
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const didUpdate = useCallback(
+    (prevProps, prevState) => {
+      if (condition) {
+        callback(prevProps, prevState);
+      }
+    },
+    [callback
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const result = useRef({
+    prevProps: null,
+    prevState: null,
+  });
+
+  if (condition) {
+    callback();
+  }
+
+  useEffect(() => {
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const componentDidUpdate = (prevProps, prevState) => {
+    if (condition(prevProps, prevState)) {
+      callback(prevProps, prevState);
+    }
+  };
+
```

#### useComponentDidUpdate (task/54)

```diff
-const useComponentDidUpdate = (callback, condition) => {
+const useComponentDidUpdate = (callback, condition) => {
+
+  const prevProps = useRef(props);
+  const prevState = useRef(state);
+
+  useEffect(() => {
+    if (condition(prevProps.current, prevState.current))
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [isToggled, setIsToggled] = useState(defaultToggled);
+
+  const toggle = () => setIsToggled(!isToggled);
+
+  return (
+   
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const handleClick = () => {
+    setToggled(!toggled);
+  };
+
+  return
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const toggle = () => setToggled(!toggled);
+
+  return (
+    <Container onClick
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [toggled, setToggled] = useState(defaultToggled);
+
+  const handleClick = () => {
+    setToggled(!toggled);
+  };
+
+  return
```

#### Toggle (task/55)

```diff
-const Toggle = ({ defaultToggled = false }) => {
+const Toggle = ({ defaultToggled = false }) => {
+
+  const [isToggled, setIsToggled] = useState(defaultToggled);
+
+  const handleToggle = () => {
+    setIsToggled(!isToggled);
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const mappedTableData = data.map(item => {
+    const mappedItem = {};
+    propertyNames.forEach(propertyName => {
+      mappedItem[propertyName] = item[propertyName];
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const { getMappedData } = useBulkActions();
+  const mappedData = getMappedData(data, propertyNames);
+  return <BulkTable data={mappedData} />;
+};
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const { data: mappedData, columns } = useTable(data, propertyNames);
+  return (
+    <table>
+      <thead>
+        <tr>
+          {columns.map((column
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  const mappedArray = data.map(row => {
+    return propertyNames.map(propertyName => {
+      return (
+        <tr key={propertyName}>
+          <td>{propertyName}</
```

#### MappedTable (task/56)

```diff
-const MappedTable = ({ data, propertyNames }) => {
+const MappedTable = ({ data, propertyNames }) => {
+
+  return (
+    <TableWrapper>
+      <Table>
+        <thead>
+          <tr>
+            {propertyNames.map(propertyName => (
+              <TableHeader key={propertyName}
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  el.addEventListener(type, handler);
+  return () => el.removeEventListener(type, handler);
+};
+
+const useEffect = (callback, dependencies) => {
+  useLayoutEffect(callback
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  const callback = event => handler(event);
+  useEffect(() => {
+    el.addEventListener(type, callback);
+    return () => {
+      el.removeEventListener(type, callback);
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+    el.addEventListener(type, handler);
+    return () => el.removeEventListener(type, handler);
+};
+
+class ProjectRow extends Component {
+    constructor(props) {
+        super(
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  el.addEventListener(type, handler);
+  return () => el.removeEventListener(type, handler);
+};
+
+const preventHtml5Dnd = (event) => {
+  event.pre
```

#### useEventListener (task/57)

```diff
-const useEventListener = (type, handler, el = window) => {
+const useEventListener = (type, handler, el = window) => {
+
+  const listener = (event) => handler(event);
+  el.addEventListener(type, listener);
+  return () => el.removeEventListener(type, listener);
+};
+
+export default useEventListener
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <ButtonBase
+      href={`tel:${phone}`}
+      onClick={(e) => {
+        e.preventDefault();
+        sendGAEvent('callto-button
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <a
+      href={`tel:${phone}`}
+      className="text-theme-7 text-lg leading-7 font-medium hover:text-theme-9"
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <a href={`tel:${phone}`}>
+      <button className="button">{children}</button>
+    </a>
+  );
+};
+
+export default Call
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <Link href={`tel:${phone}`}>
+      <a className="callto">{children}</a>
+    </Link>
+  );
+};
+
+export default
```

#### Callto (task/58)

```diff
-const Callto = ({ phone, children }) => {
+const Callto = ({ phone, children }) => {
+
+  return (
+    <a
+      href={`tel:${phone}`}
+      target="_blank"
+      rel="noopener noreferrer"
+      className="callto"
+   
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+	useEffect(() => {
+		const handleResize = () => {
+			callback();
+		};
+		window.addEventListener('resize', handleResize);
+		return
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+  const windowResizeEvent = () => {
+    callback();
+  };
+
+  window.addEventListener('resize', windowResizeEvent);
+
+  return () => {
+    window.removeEventListener('res
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+	const handleResize = () => {
+		const { innerWidth: width, innerHeight: height } = window;
+		callback({ width, height });
+	};
+
+	useEffect(() => {
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+	const eventName = 'resize';
+	const listener = () => {
+		const node = window;
+		const win = node.window;
+		const doc = node.document;
+		
```

#### useOnWindowResize (task/59)

```diff
-const useOnWindowResize = callback => {
+const useOnWindowResize = callback => {
+
+  const resizeTimer = {};
+  const onResize = (window.innerWidth, window.innerHeight) => {
+    clearTimeout(resizeTimer.timer);
+    resizeTimer.timer = setTimeout(
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  const handleChange = e => {
+    setValue(e.target.value);
+    onValueChange(e.target.value);
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  const onChange = (event) => {
+    setValue(event.target.value);
+    onValueChange(event.target.value
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  const handleChange = (e) => {
+    const { value } = e.target;
+    setValue(value);
+    onValue
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  const handleChange = e => {
+    setValue(e.target.value);
+    onValueChange(e.target.value);
```

#### UncontrolledInput (task/60)

```diff
-const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
+
+  const [value, setValue] = useState(defaultValue)
+
+  useEffect(() => {
+    if (value !== defaultValue) {
+      setValue(defaultValue)
+    }
+  },
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+
+  name,
+  label,
+  onChange,
+  placeholder,
+  error,
+  value,
+  rows,
+  cols,
+  id,
+  style,
+  type,
+  valueType
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ name, label, error, ...rest }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        {
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ name, value, onChange, placeholder, error, rows }) => {
+  return (
+    <div className="form-group">
+      <textarea
+        className="form-control"
+        placeholder={placeholder
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ name, label, error, ...rest }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        {
```

#### TextArea (task/61)

```diff
-const TextArea = ({
+const TextArea = ({
+ name, label, error, ...rest }) => {
+  return (
+    <div className="form-group">
+      <label htmlFor={name}>{label}</label>
+      <textarea
+        {
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  const [ready, setReady] = useState(false)
+  const [failed, setFailed] = useState(false)
+
+  useEffect(() => {
+    if (!ready && !failed) {
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  // We create a new script element.
+  const script = document.createElement('script');
+  script.async = true;
+  script.src = src;
+
+  // Then append it to the DOM.
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  useEffect(() => {
+    const script = document.createElement('script');
+    script.src = src;
+    script.async = true;
+    document.body.appendChild(script);
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  useEffect(() => {
+    if (!document.getElementById(src)) {
+      const script = document.createElement('script');
+      script.id = src;
+      script.src = src;
```

#### useScript (task/62)

```diff
-const useScript = src => {
+const useScript = src => {
+
+  useEffect(() => {
+    const s = document.createElement('script');
+    s.src = src;
+    s.async = true;
+    document.body.appendChild(s);
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  useEffect(() => {
+    const handle = requestAnimationFrame(callback);
+    return () => cancelAnimationFrame(handle);
+  }, [callback]);
+};
+
+const PostDetails = ({ match }) => {
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+    const handle = requestAnimationFrame(callback);
+    return () => cancelAnimationFrame(handle);
+};
+
+export const toPercent = (min, max, value) => {
+    return ((value - min) /
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  useEffect(() => {
+    let requestId;
+    const animationFrame = () => {
+      requestId = requestAnimationFrame(animationFrame);
+      callback();
+    };
+    requestId = request
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  const requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
+  const raf = requestAnimationFrame(callback);
+ 
```

#### useRequestAnimationFrame (task/63)

```diff
-const useRequestAnimationFrame = callback => {
+const useRequestAnimationFrame = callback => {
+
+  let requestAnimationFrame;
+  let canceled = false;
+  let isCanceled = () => canceled;
+  const raf = (...args) => {
+    if (canceled) return;
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [value, setValue] = useState(initialValue);
+  return [value, setValue];
+};
+
+const useToggle = initialValue => {
+  const [value, setValue] = use
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+    const [state, setState] = useState(initialValue);
+    return [state, setState];
+};
+
+export default useSet;
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  return [state, setState];
+};
+
+export default useSet;
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [data, setData] = useState(initialValue);
+  return [data, setData];
+};
+
+export const useAuth = () => {
+  const [data, setData] = useState
```

#### useSet (task/64)

```diff
-const useSet = initialValue => {
+const useSet = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  return [state, setState];
+};
+
+const reducer = (state, action) => {
+  switch (action.type) {
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(
+    localStorage.getItem(keyName) || defaultValue
+  );
+
+  const setValueToLocalStorage = value => {
+    localStorage.setItem
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(defaultValue);
+
+  useEffect(() => {
+    const storageValue = localStorage.getItem(keyName);
+    if (storageValue) {
+     
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    try {
+      const item = window.localStorage.getItem(keyName);
+      return item ? JSON.parse(item) : default
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  if (typeof window === 'undefined') return defaultValue;
+  if (!localStorage.getItem(keyName)) {
+    localStorage.setItem(keyName, JSON.stringify(defaultValue));
```

#### useLocalStorage (task/65)

```diff
-const useLocalStorage = (keyName, defaultValue) => {
+const useLocalStorage = (keyName, defaultValue) => {
+
+  const [value, setValue] = useState(() => {
+    try {
+      const storageValue = localStorage.getItem(keyName);
+      if (storageValue) {
+        return JSON.parse
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const [height, setHeight] = useState(null);
+  const node = useRef();
+
+  useEffect(() => {
+    if (!collapsed) {
+      setHeight(node.current.scroll
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const classes = useStyles();
+  const theme = useTheme();
+  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
+
+  const [open, setOpen] = useState
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const [open, setOpen] = useState(false);
+
+  const handleClick = () => {
+    setOpen(!open);
+  };
+
+  return (
+    <>
+      <div
+       
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const classes = useStyles();
+  const theme = useTheme();
+  const [open, setOpen] = React.useState(false);
+
+  const handleClick = () => {
+    setOpen(!
```

#### Collapse (task/66)

```diff
-const Collapse = ({ collapsed, children }) => {
+const Collapse = ({ collapsed, children }) => {
+
+  const collapseStyles = {
+    overflow: 'hidden',
+    height: '0px',
+    padding: '0',
+    transition: 'height .4s ease',
+  };
+
+  const expandedSty
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const classes = useStyles();
+  return (
+    <div className={classes.root}>
+      <div className={classes.content}>
+        <Button onClick={onClick}>{
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [hover, setHover] = useState(false);
+  const onMouseEnter = () => setHover(true);
+  const onMouseLeave = () => setHover(false);
+
+  return
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [, updateState] = useState();
+  const [startTransition] = useTransition(() => Date.now(), null, {
+    from: {
+      opacity: 0,
+      transform:
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [startRipple, setStartRipple] = useState(false);
+  const rippleRef = useRef(null);
+
+  const classes = classNames({
+    'whitespace-no-wrap text
```

#### RippleButton (task/67)

```diff
-const RippleButton = ({ children, onClick }) => {
+const RippleButton = ({ children, onClick }) => {
+
+  const [isPressed, setIsPressed] = useState(false);
+
+  const onButtonPress = () => {
+    setIsPressed(true);
+    onClick();
+  };
+
+  const
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+
+  container: HTMLElement,
+  callback: (event: MutationObserverInit) => void
+) => {
+  const mutationObserver = new MutationObserver(callback);
+  mutationObserver.
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+element: Element | null) => {
+  const observer = new MutationObserver(() => {
+    const array = Array.from(element?.children ?? []);
+    element?.children = array;
+ 
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+): [boolean, Function] => {
+  const isSupported = typeof MutationObserver !== 'undefined';
+  const isMutated = false;
+
+  if (isSupported) {
+    const callback =
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+ref: any) => {
+  const mutationObserver = new MutationObserver(() => {
+    if (ref.current) {
+      scrollToRef(ref)
+    }
+  })
+
+  return mutation
```

#### useMutationObserver (task/68)

```diff
-const useMutationObserver = (
+const useMutationObserver = (
+element, callback) => {
+  const handleRefresh = () => {
+    callback(element);
+  };
+
+  useEffect(() => {
+    const observer = new MutationObserver(handleRefresh);
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <div className="tooltip" {...rest}>
+      {children}
+      <span className="tooltiptext">{text}</span>
+    </div>
+ 
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <div className="tooltip" {...rest}>
+      {children}
+      <span className="tooltiptext">{text}</span>
+    </div>
+ 
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipWrapper {...rest}>
+      {children}
+      <TooltipText>{text}</TooltipText>
+    </TooltipWrapper>
+  );
+};
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <Wrapper {...rest}>
+      {children}
+      <Text>{text}</Text>
+    </Wrapper>
+  );
+};
+
+export default Tooltip;
```

#### Tooltip (task/69)

```diff
-const Tooltip = ({ children, text, ...rest }) => {
+const Tooltip = ({ children, text, ...rest }) => {
+
+  return (
+    <TooltipWrapper {...rest}>
+      {children}
+      <TooltipText>{text}</TooltipText>
+    </TooltipWrapper>
+  );
+};
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const timer = setTimeout(callback, delay);
+  return () => clearTimeout(timer);
+};
+
+const useFocus = (ref, onFocus) => {
+  const handleFocus = useCallback(() =>
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useTimeout (task/70)

```diff
-const useTimeout = (callback, delay) => {
+const useTimeout = (callback, delay) => {
+
+  const savedCallback = useRef();
+
+  // Remember the latest callback.
+  useEffect(() => {
+    savedCallback.current = callback;
+  }, [callback]);
+
+  // Set up the interval.
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  useEffect(() => {
+    console.log(err);
+  }, [err]);
+};
+
+export default useError;
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+	if (typeof err === 'string') {
+		return {
+			value: undefined,
+			hasError: true,
+			type: 'string',
+			message:
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  const [error, setError] = useState(err);
+  return [error, setError];
+};
+
+const useActiveUser = () => {
+  const [activeUser, setActiveUser] = use
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  const [state, setState] = useState({
+    status: "",
+    message: "",
+  });
+
+  useEffect(() => {
+    if (err) {
+      setState({
```

#### useError (task/71)

```diff
-const useError = err => {
+const useError = err => {
+
+  const [error, setError] = useState(err);
+  return [error, setError];
+};
+
+export default useError;
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [copied, setCopied] = useState(false);
+  const handleClick = () => {
+    setCopied(true);
+    copy(text);
+    setTimeout(() => setCop
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+	const [copied, setCopied] = useState(false);
+
+	const copyToClipboard = () => {
+		const textArea = document.createElement('textarea');
+		textArea
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [copied, setCopied] = useState(false);
+  const onCopy = () => {
+    setCopied(true);
+    setTimeout(() => setCopied(false), 2000);
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [isCopied, setIsCopied] = useState(false);
+
+  const handleCopy = () => {
+    navigator.clipboard.writeText(text);
+    setIsCopied(true
```

#### useCopyToClipboard (task/72)

```diff
-const useCopyToClipboard = text => {
+const useCopyToClipboard = text => {
+
+  const [isCopied, setIsCopied] = useState(false);
+
+  const copyToClipboard = () => {
+    copy(text);
+    setIsCopied(true);
+    set
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const store = useRef({
+    ...initialValue,
+    get: key => store.current[key],
+    set: (key, value) => (store.current[key] = value),
+    remove
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+	let key = 0;
+	return {
+		map: new Map(),
+		set: value => {
+			const nextKey = key++;
+			const nextValue = initialValue ? initial
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const [map, setMap] = useState(initialValue);
+
+  const getMap = () => map;
+
+  const setMapValue = (key, value) => {
+    setMap({
+      ...map
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const [state, setState] = useState(initialValue);
+  const set = key => value => {
+    setState({
+      ...state,
+      [key]: value,
+    });
+  };
```

#### useMap (task/73)

```diff
-const useMap = initialValue => {
+const useMap = initialValue => {
+
+  const [results, setResults] = useState(initialValue);
+
+  const add = (...args) => {
+    const key = args[0];
+    if (key === undefined) {
+      throw new
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const handleClick = useCallback(() => {
+    window.open(text);
+  }, [text]);
+
+  return (
+    <Button size="small" variant="outlined" onClick={handleClick}
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  return (
+    <a
+      href={`https://www.google.com/search?q=${text}`}
+      target="_blank"
+      rel="noopener noreferrer"
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const { email } = parse(text);
+  const isEmail = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const output = text.split(' ').map((word) => {
+    if (word.match(/^https?:\/\//)) {
+      return (
+        <a
+          key={word}
```

#### AutoLink (task/74)

```diff
-const AutoLink = ({ text }) => {
+const AutoLink = ({ text }) => {
+
+  const Link = props => {
+    const match = props.match.match(/(?<=^|\s|\()([\w\.\:\/]+)/)
+    if (match && isValidURL
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+    const [debouncedValue, setDebouncedValue] = useState(value);
+
+    useEffect(() => {
+        const handler = setTimeout(() => {
+            setDebouncedValue(value);
+       
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+   
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+   
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+    const [debouncedValue, setDebouncedValue] = useState(value);
+
+    useEffect(() => {
+        const handler = setTimeout(() => {
+            setDebouncedValue(value);
+       
```

#### useDebounce (task/75)

```diff
-const useDebounce = (value, delay) => {
+const useDebounce = (value, delay) => {
+
+  const [debouncedValue, setDebouncedValue] = useState(value);
+
+  useEffect(() => {
+    const handler = setTimeout(() => {
+      setDebouncedValue(value);
+   
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [data, setData] = useState(null);
+  const [error, setError] = useState(null);
+  const [loading, setLoading] = useState(false);
+
+  useEffect
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [data, setData] = useState(null);
+  const [loading, setLoading] = useState(true);
+  const [error, setError] = useState(null);
+
+  useEffect
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [data, setData] = useState(null);
+  const [error, setError] = useState(null);
+  const [loading, setLoading] = useState(false);
+
+  useEffect
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [response, setResponse] = useState(null);
+  const [error, setError] = useState(null);
+  const [isLoading, setIsLoading] = useState(false);
+
+ 
```

#### useFetch (task/76)

```diff
-const useFetch = (url, options) => {
+const useFetch = (url, options) => {
+
+  const [response, setResponse] = useState({})
+  const [error, setError] = useState(null)
+  const [isLoading, setIsLoading] = useState(false)
+
+  use
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  const callbackRef = useRef();
+  useEffect(() => {
+    const el = document.body;
+    const handleEvent = () => {
+      callbackRef.current();
+    };
+    el.
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  if (useGlobalEventListeners[type]) {
+    throw new Error(`The event ${type} is already being listened`);
+  }
+
+  const { once } = options || {};
+
+  useEffect
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  const handler = (e) => {
+    if (e.type === type) {
+      callback(e);
+    }
+  };
+
+  window.addEventListener(type, handler, options);
+
+ 
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  const { capture = false, once = false } = options || {}
+  const handle = (event) => {
+    if (event.type === type) {
+      callback(event)
+      if (once)
```

#### useOnGlobalEvent (task/77)

```diff
-const useOnGlobalEvent = (type, callback, options) => {
+const useOnGlobalEvent = (type, callback, options) => {
+
+  const event = typeof type === 'string' ? new CustomEvent(type, options) : type
+  document.addEventListener(event.type, callback)
+  return () => document.removeEventListener(event
```

